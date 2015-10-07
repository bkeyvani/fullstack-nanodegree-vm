"""
Model classes which define DB tables for the project.
"""

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

movie_genres = Table(
    'movie_genres', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.id')))

class Movie(Base):
    """
    Model representing Movie table in the DB.
    """
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    poster_image_url = Column(String(255), nullable=False)
    trailer_youtube_url = Column(String(255), nullable=False)
    storyline = Column(Text, nullable=False)
    mpaa_rating_id = Column(Integer, ForeignKey('mpaa_ratings.id'))
    duration = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)
    imdb_id = Column(String(80))
    rotten_id = Column(String(80))

    # many-to-many Movie<->Genre
    genres = relationship("Genre", secondary=movie_genres, backref="movies")

    def __repr__(self):
        return "<Movie: %r>" % self.title


class Genre(Base):
    """
    Model representing Genre table in the DB.
    """
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return "<Genre: %r>" % self.name


class MPAARatings(Base):
    """
    Model representing Genre table in the DB.
    """
    __tablename__ = 'mpaa_ratings'

    id = Column(Integer, primary_key=True)
    rating = Column(String(10), nullable=False, unique=True)
    movies = relationship("Movie")

    def __repr__(self):
        return "<Rating: %r>" % self.name

engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)
