from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
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
    picture = Column(String(255))
    weight = Column(Float(5))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)

    def __repr__(self):
        return "<Puppy: %r, id: %r>" % (self.name, self.id)

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
