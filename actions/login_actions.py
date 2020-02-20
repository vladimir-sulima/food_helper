from flask import request, session, flash
from passlib.handlers.sha2_crypt import sha256_crypt

from models.user import User


def validate_login(opened_session, app):
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        user_candidate = opened_session.query(User).filter_by(user_name=username).first()
        if user_candidate is not None:
            password = user_candidate.password
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username

                # flash('You are now logged in', 'success')
                return "success"
            else:
                return "error"
        else:
            return "error"
