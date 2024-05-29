from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username')
    email = StringField('E-mail')
    password = PasswordField('Password')
    retypePassword = PasswordField('Retype password')
