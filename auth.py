import os
from flask import Blueprint, session, redirect, url_for, render_template
from forms import LoginForm, RegisterForm
from models import User
from passenger_wsgi import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mailman import EmailMessage

auth = Blueprint('auth', __name__)
mail_email = os.getenv('MAIL_EMAIL')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('admin.dashboard'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.password, form.password.data):
                session['id'] = user.uid
                session['name'] = user.name
                session['email'] = user.email
                session['role'] = user.role
                session['loggedin'] = True
                return redirect(url_for('site.index'))
        return render_template('login.html', form=form)


@auth.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('auth.login'))


@auth.route("/register", methods=['GET', 'POST'])
def register():
    msg = ''
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password, role="admin")
        db.session.add(new_user)
        db.session.commit()
        msg = f'Thank you, {form.name.data}, for registering. An email will be sent to {form.email.data}.'
        email_msg = EmailMessage(
            'Thank You for Registering',
            'You have successfully registered your account. Please go to ' + url_for("login") + ' to log in.',
            mail_email,
            [form.email.data],
            headers={'Message-ID': 'foo'},
        )
        email_msg.send()
    return render_template('register.html', form=form, msg=msg)
