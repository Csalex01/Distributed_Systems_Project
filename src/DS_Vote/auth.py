from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
from flask_bcrypt import check_password_hash, generate_password_hash

from DS_Vote.models import *

auth = Blueprint("auth", __name__)

class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": "E-mail"})
    password = PasswordField('Password', render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', render_kw={"placeholder": "First name"})
    last_name = StringField('Last Name', render_kw={"placeholder": "Last name"})
    email = StringField('Email', render_kw={"placeholder": "E-mail"})
    password = PasswordField('Password', render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            print("AFTER VALIDATION")

            user = Users.query.filter_by(Email=form.email.data).first()

            if user and check_password_hash(user.Password, form.password.data):
                login_user(user)

            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
                
            return redirect(url_for('base.index'))

    elif request.method == 'GET':
        return render_template('auth/login.html', form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("base.index"))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == "POST":

        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data).decode('utf-8')

            user = Users(
                Email=form.email.data, 
                Password=hashed_password, 
                FirstName=form.first_name.data, 
                LastName=form.last_name.data
            )
            
            db.session.add(user)
            db.session.commit()

            flash(f'Account created for {form.first_name.data}!', 'success')

            return redirect(url_for('auth.login'))

    elif request.method == "GET":
        return render_template('auth/register.html', form=form)