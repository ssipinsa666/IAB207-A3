from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#Create new event
class EventForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
  price = StringField('price', validators=[InputRequired()])
  date = DateField('date', validators=[InputRequired()])
  location = StringField('location', validators=[InputRequired()])
  category = StringField('category', validators=[InputRequired()])
  status = StringField('status', validators=[InputRequired()])
  organizer_id = StringField('organizer_id', validators=[InputRequired()])
  submit = SubmitField("Create")


# creates the login information
class LoginForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    # linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    contact_number=StringField("Contact_number", validators=[InputRequired()])

    # submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  content = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')