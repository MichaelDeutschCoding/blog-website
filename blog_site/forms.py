from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, validators


class LoginForm(FlaskForm):
    email = StringField('E-Mail')
    password = PasswordField('Password')


class RegistrationForm(FlaskForm):
    email = StringField('E-Mail', [validators.required()])
    password = PasswordField('Password', [validators.required()])
    confirm_password = PasswordField('Confirm Password', [validators.required()])
    first_name = StringField('First Name', [validators.required()])
    last_name = StringField('Last Name', [validators.required()])
    username = StringField('Choose a User Name', [validators.Length(min=6, max=25)])


class BlogForm(FlaskForm):
    title = StringField('Title', [validators.required()])
    content = TextAreaField('Blog Content', [validators.required()])
    tags = StringField(label='Tags', description='Enter any number of tags, separated with a comma.')