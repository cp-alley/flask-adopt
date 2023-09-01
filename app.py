"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

from models import connect_db, Pet, db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_home_page():
    """Shows list of all pets"""
    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_new_pet():
    """Process the add form, adding a new pet and going back to home page"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age, notes=notes,
                  available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet details, pet edit form, and handle form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return render_template('pet_detail.html', form=form, pet=pet)

    else:
        # redirect('/pets/{pet_id}')
        return render_template('pet_detail.html', pet=pet, form=form)
