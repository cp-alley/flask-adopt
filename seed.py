from app import app
from models import DEFAULT_IMAGE_URL, Pet, db


db.drop_all()
db.create_all()

# For testing database initially
buddy = Pet(name='Buddy', species="dog", age="senior", notes="He was a good dog.", available=False)
nemo = Pet(name="Nemo", species="clownfish", age="young", notes="He touched the butt")

db.session.add(buddy)
db.session.add(nemo)
db.session.commit()