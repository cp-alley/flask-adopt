"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, BooleanField

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species of Pet")
    photo_url = StringField("Photo of Pet, if Available")
    age = SelectField("Age of Pet", choices=[('baby', 'baby'), ('young', 'young'), ('adult', 'adult'), ('senior', 'senior')])
    notes = StringField("Notes/Comments on pet, if any")
    available = BooleanField("Is pet currently available to adopt?")