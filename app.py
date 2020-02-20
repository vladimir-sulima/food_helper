from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from actions import storage_actions, item_actions
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

from actions.login_actions import validate_login
from data.session_factory import get_session
from forms.registration_form import RegisterForm, add_new_user
from models.user import User

app = Flask(__name__)
app.debug = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/storage')
def storage():
    with get_session() as opened_session:
        storage_list = storage_actions.get_storage_list(opened_session)
        return render_template('storage.html', storage=storage_list)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/storage/<string:id>/')
def item_in_particular_storage(id):
    with get_session() as opened_session:
        items_list = item_actions.get_items_by_storage_id(id, opened_session)
        storage_name = storage_actions.get_storage_title_by_id(id, opened_session)
        return render_template('single_storage.html', items_list=items_list, storage_name=storage_name)


@app.route('/register', methods=['GET', 'POST'])
def register():
    with get_session() as opened_session:
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            add_new_user(form, opened_session)
            return render_template('home.html')
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    with get_session() as opened_session:
        result = validate_login(opened_session, app)
        if result == 'error':
            return render_template('login.html', error="Username or password not matched. Try again, please.")
        elif result == 'success':
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':

    app.run()


