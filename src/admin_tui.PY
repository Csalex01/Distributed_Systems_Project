from DS_Vote import db, app
from DS_Vote.models import Users, Votes
from DS_Vote.helpers import COLORS, clear_screen

from werkzeug.security import generate_password_hash, check_password_hash

# Push application context      
ctx = app.app_context()
ctx.push()

def print_users():
    users = Users.query.all()

    print(f"\n{COLORS.OKGREEN}Users\n*--------*{COLORS.RESET}")

    for idx, user in enumerate(users):
        print(f"{COLORS.OKCYAN}{idx + 1}. User ID: {user.UserID}{COLORS.RESET}")
        print(f"\tEmail: {user.Email}")
        print(f"\tName: {user.FirstName} {user.LastName}")
        print("")

def print_votes():
    votes = Votes.query.all()

    print(f"\n{COLORS.OKGREEN}Votes\n*--------*{COLORS.RESET}")

    for idx, vote in enumerate(votes):
        print(f"{COLORS.OKCYAN}{idx + 1}. Vote ID: {vote.VoteID}{COLORS.RESET}")
        print(f"\tUser ID: {vote.UserID}")
        print(f"\tWhiteGold: {vote.WhiteGold}")
        print(f"\tBlueBlack: {vote.BlueBlack}")
        print(f"\tOther: {vote.Other}")
        print("")

def sign_up():
    print(f"\n{COLORS.OKGREEN}Sign Up{COLORS.RESET}")

    email = input(f"{COLORS.OKGREEN}> Email: {COLORS.OKCYAN}")
    password = input(f"{COLORS.OKGREEN}> Password: {COLORS.OKCYAN}")
    first_name = input(f"{COLORS.OKGREEN}> First Name: {COLORS.OKCYAN}")
    last_name = input(f"{COLORS.OKGREEN}> Last Name: {COLORS.OKCYAN}")

    try:
        user = Users(Email=email, Password=generate_password_hash(password), FirstName=first_name, LastName=last_name)
        db.session.add(user)
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nUser added successfully!{COLORS.RESET}")

    except Exception as e:
        print(f"{COLORS.FAIL}\nError: {e}{COLORS.RESET}")

def create_vote():
    print(f"\n{COLORS.OKGREEN}Create Vote{COLORS.RESET}")

    user_id = input(f"{COLORS.OKGREEN}> User ID: {COLORS.OKCYAN}")
    user = Users.query.filter_by(UserID=user_id).first()

    if user is None:
        print(f"\n{COLORS.FAIL}Error: User {user_id} does not exist!{COLORS.RESET}")
        return

    white_gold = input(f"{COLORS.OKGREEN}> WhiteGold (True/False): {COLORS.OKCYAN}")
    blue_black = input(f"{COLORS.OKGREEN}> BlueBlack (True/False): {COLORS.OKCYAN}")
    other = input(f"{COLORS.OKGREEN}> Other: {COLORS.OKCYAN}")

    votes = Votes.query.all()
    
    for vote in votes:
        if vote.UserID == user.UserID:
            print(f"\n{COLORS.FAIL}Error: User {user.UserID} has a vote!{COLORS.RESET}")
            return

    white_gold = True if white_gold.lower() == "true" or white_gold == "1" else False
    blue_black = True if blue_black.lower() == "true" or blue_black == "1" else False

    try:
        vote = Votes(UserID=user_id, WhiteGold=white_gold, BlueBlack=blue_black, Other=other)
        db.session.add(vote)
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nVote added successfully!{COLORS.RESET}")

    except Exception as e:
        print(f"{COLORS.FAIL}\nError: {e}{COLORS.RESET}")

def update_vote():
    print(f"\n{COLORS.OKGREEN}Update Vote{COLORS.RESET}")

    vote_id = input(f"{COLORS.OKGREEN}> Vote ID: {COLORS.OKCYAN}")
    vote = Votes.query.filter_by(VoteID=vote_id).first()

    if vote is None:
        print(f"\n{COLORS.FAIL}Error: Vote {vote_id} does not exist!{COLORS.RESET}")
        return

    white_gold = input(f"{COLORS.OKGREEN}> WhiteGold (True/False): {COLORS.OKCYAN}")
    blue_black = input(f"{COLORS.OKGREEN}> BlueBlack (True/False): {COLORS.OKCYAN}")
    other = input(f"{COLORS.OKGREEN}> Other: {COLORS.OKCYAN}")

    white_gold = True if white_gold.lower() == "true" or white_gold == "1" else False
    blue_black = True if blue_black.lower() == "true" or blue_black == "1" else False

    try:
        vote.WhiteGold = white_gold
        vote.BlueBlack = blue_black
        vote.Other = other
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nVote updated successfully!{COLORS.RESET}")

    except Exception as e:
        print(f"{COLORS.FAIL}\nError: {e}{COLORS.RESET}")

def delete_user():
    print(f"\n{COLORS.OKGREEN}Delete User{COLORS.RESET}")

    user_id = input(f"{COLORS.OKGREEN}> User ID: {COLORS.OKCYAN}")

    try:
        user = Users.query.filter_by(UserID=user_id).first()
        db.session.delete(user)
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nUser deleted successfully!{COLORS.RESET}")

    except Exception as e:
        print(f"{COLORS.FAIL}\nError: {e}{COLORS.RESET}")

def delete_vote():
    print(f"\n{COLORS.OKGREEN}Delete Vote{COLORS.RESET}")

    vote_id = input(f"{COLORS.OKGREEN}> Vote ID: {COLORS.OKCYAN}")

    try:
        vote = Votes.query.filter_by(VoteID=vote_id).first()
        db.session.delete(vote)
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nVote deleted successfully!{COLORS.RESET}")

    except Exception as e:
        print(f"{COLORS.FAIL}\nError: {e}{COLORS.RESET}")

# Method for menu
def menu():
    while True:

        print(f"\n{COLORS.OKCYAN}*--------* DS_Vote Database TUI *--------*{COLORS.RESET}")
        print(f"{COLORS.WARNING}*-----------* LOG *-----------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}1.){COLORS.RESET} Print Users")
        print(f"{COLORS.OKGREEN}2.){COLORS.RESET} Print Votes")
        print(f"{COLORS.WARNING}*-----* Add to Database *-----*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}3.){COLORS.RESET} Sign Up User")
        print(f"{COLORS.OKGREEN}4.){COLORS.RESET} Create Vote")
        print(f"{COLORS.OKGREEN}5.){COLORS.RESET} Update Vote")
        print(f"{COLORS.WARNING}*-----* Delete from Database *-----*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}6.){COLORS.RESET} Delete User")
        print(f"{COLORS.OKGREEN}7.){COLORS.RESET} Delete Vote")
        print(f"{COLORS.WARNING}*-----------------------------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}0.){COLORS.RESET} Exit")
        print(f"{COLORS.OKCYAN}*--------------------------------------------------*{COLORS.RESET}")

        try:
            choice = int(input(f"{COLORS.OKGREEN}> Choice: {COLORS.OKCYAN}"))

        except ValueError:
            clear_screen()
            print(f"\n{COLORS.FAIL}Invalid input! Numbers only.{COLORS.RESET}")
            continue

        except KeyboardInterrupt:
            clear_screen()
            print(f"{COLORS.FAIL}\nQuit.{COLORS.RESET}\n")
            return

        clear_screen()

        if choice == 1:
            print_users()

        elif choice == 2:
            print_votes()

        elif choice == 3:
            sign_up()

        elif choice == 4:
            create_vote()

        elif choice == 5:
            update_vote()

        elif choice == 6:
            delete_user()

        elif choice == 7:
            delete_vote()

        elif choice == 0:
            print(f"{COLORS.FAIL}\nQuit.{COLORS.RESET}\n")
            exit()
        
        else:
            print(f"\n{COLORS.FAIL}Invalid input!{COLORS.RESET}")

# Start the menu
clear_screen()
menu()

# Pop application context
ctx.pop()