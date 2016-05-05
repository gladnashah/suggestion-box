from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Email, Regexp, EqualTo


class LoginForm(Form):
	email = StringField('Email', validators=[Required(),Email()])
	username = StringField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('keep me looged in')
	submit = SubmitField('Log In')

class RegistrationForm(Form):
	email = StringField('Email', validators=[Required(),Email()])

	username = StringField('Username', validators=[Required(), 
		 Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
							'Usernames must have only letters, '
							'numbers, dots or underscores')])

	password = PasswordField('Password', validators=[
		Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class PostForm(Form):
	title = StringField('Your suggestion title here', validators=[Required()])
	body = TextAreaField("What's on your mind?", validators=[Required()])
	submit = SubmitField('Submit')