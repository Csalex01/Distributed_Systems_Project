from DS_Vote.models import *

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import current_user, login_required

vote = Blueprint("vote", __name__)

class VoteForm(FlaskForm):
    vote = RadioField(
        'What color is the dress?', 
        choices=[
            ("wg", "White & Gold"), 
            ("bb", "Black & Blue")
        ],
        render_kw={"class": "test"},
        validators=[DataRequired()],
    )
    submit = SubmitField('Vote')

@vote.route("/vote", methods=['GET', 'POST'])
def new_vote():
    form = VoteForm()

    if request.method == "POST":

        print(form.data)

        vote = Votes(
            UserID=current_user.UserID,
            WhiteGold=form.vote.data == 'wg',
            BlueBlack=form.vote.data == 'bb',
        )

        db.session.add(vote)
        db.session.commit()

        return redirect(url_for("base.index"))

    elif request.method == 'GET':
        return render_template("vote/vote.html", form=form)