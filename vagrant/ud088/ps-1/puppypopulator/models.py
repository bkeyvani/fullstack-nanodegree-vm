from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Shelter(Base):
    """
    Model representing a Shelter table in the DB
    """
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    address = Column(String(200))
    city = Column(String(80))
    state = Column(String(80))
    zipcode = Column(String(10))
    website = Column(String(255))

    def __repr__(self):
        return "<Shelter: %r>" % self.name


association_table = Table('associatio', Base.metadata,
        Column('puppy_id', Integer, ForeignKey('puppy.id')),
        Column('adopter_id', Integer, ForeignKey('adopter.id')))


class Puppy(Base):
    """
    Model representing a Puppy table in the DB
    """
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    bread = Column(String(80))
    gender = Column(String(10), nullable=False)
    weight = Column(Float(5))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship("Shelter")
    profile = relationship("Profile", uselist=False, backref="profile")
    adopters = relationship("adopter",
            secondary=association_table,
            backref="puppy")

    def __repr__(self):
        return "<Puppy: %r, id: %r>" % (self.name, self.id)


class Profile(Base):
    """
    Model representing a Profile for each puppy.
    """
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    photo_url = Column(String(255))
    description = Column(String)
    special_needs = Column(String)

    def __repr__(self):
        return "<Profile for puppy: %r>" % self.puppy_id

class Adopter(Base):
    """
    Model representing an adopter for a puppy.
    """
    __tablename__ = 'adopter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def __repr__(self):
        return "<Adopter: %r>" % self.name


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
