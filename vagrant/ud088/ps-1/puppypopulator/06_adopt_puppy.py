from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import label

from models import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

q = session.query(Puppy)

# TODO: Create a method for adopting a puppy based on its id. the method should
# also take in an array of adopter ids of the family members who will be
# responsible for the puppy. An adopted puppy should stay in the puppy database
# but no longer be taking up an occupancy spot in the shelter.

def adopt_puppy(puppy, adopters=[]):
    """
    Adds the adopters to puppy and updates the shelter's occupancy that is
    holding the puppy by reducing the current_occupancy.
    """

    # throw an exception if adopters is empty

    # for each adopter in adopters, add a puppy_adopter association,

    # update puppy's shelter occupancy

    pass
