"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

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
    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)


@app.route("/pets/add", methods=["GET", "POST"])
def add_new_pet():
    """Process the add form, adding a new pet and going back to /pets"""

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
