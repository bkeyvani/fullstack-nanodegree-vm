from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import label

from models import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

q = session.query(Puppy)

# TODO: Create a function to check a puppy into a shelter, if the shelter is at
# capacity, prompt the user to try a different shelter.

def check_in(shelter_id, puppy):
    """
    Checks a puppy into the shelter with `shelter_id` and updates all fields.
    This function will throw an exception if the designated shelter is full.
    """

    # check the shelters capacity and throw exception if capacity is < 1

    # update puppy.shelter_id, increase shelter's occupancy by 1.

    pass
