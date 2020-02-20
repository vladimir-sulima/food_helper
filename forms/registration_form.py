from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from actions import storage_actions, item_actions
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

from models.user import User
from data.session_factory import create_session


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=50), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=50), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')



def add_new_user(form, session):

    user = {'name': form.name.data,
            'email': form.email.data,
            'user_name': form.username.data,
            'password': sha256_crypt.encrypt(str(form.password.data))}

    new_user = User(name=user['name'], email=user['email'], user_name=user['user_name'], password=user['password'])

    session.add(new_user)


