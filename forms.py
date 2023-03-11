from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message='Field required.')])
    password = PasswordField('Password', validators=[DataRequired(message='Field required.')])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Field required.')])
    email = EmailField('Email', validators=[DataRequired(message='Field required.')])
    password = PasswordField(
        'Password',
        validators=[
            Length(min=8),
            Regexp(
                "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@.,;:$%^&*-])",
                message='Must contain at least one of each: capital, lowercase, digit, and special character.'
            ),
            EqualTo('confirm', message='Passwords must match.')
        ]
    )
    confirm = PasswordField('Confirm your password', validators=[DataRequired(message='Field required.')])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')


class PageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Field required.')])
    text = TextAreaField('Text')
    keywords = StringField("Keywords")
    emgithub = StringField("Emgithub")
    youtube = StringField("Youtube")
    image = FileField("Image")
    type = SelectField("Type", choices=[
        ("", "Select Page Type"),
        ("page", "Page"),
        ("post", "Blog post"),
        ("entry", "Portfolio entry")
    ])
    submit = SubmitField('Submit')
