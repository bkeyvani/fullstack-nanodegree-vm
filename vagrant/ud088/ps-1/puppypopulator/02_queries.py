from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import label

from models import Base, Shelter, Puppy
import datetime


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

q = session.query(Puppy)

# 1. Query all of the puppies and return the results in ascending alphabetical
# order
all_asc = q.order_by(Puppy.name)

# 2. Query all of the puppies that are less than 6 months old organized by the youngest first
# calculate timedelta of 6 approx. months (+/- 1 day)
today = datetime.date.today()
six_months_ago = datetime.date(today.year + (today.month - 6)/12, (today.month - 6) % 12, today.day)

less_than_six_months = q.filter(Puppy.date_of_birth > six_months_ago)
less_than_six_months_asc = less_than_six_months.order_by(Puppy.date_of_birth.asc())

# 3. Query all puppies by ascending weight
puppy_by_weight_asc = q.order_by(Puppy.weight.asc())

# 4. Query all puppies grouped by the shelter in which they are staying

q4 = session.query(Shelter, Puppy)
result = q4.join(Puppy, Puppy.shelter_id == Shelter.id).\
            order_by(Shelter.name).\
            all()

# returns a list of tuples containing shelter IDs and the count of puppies in
# each shelter
counts = session.query(Shelter, label('count', func.count(Puppy.name))).\
                 group_by(Puppy.shelter_id).\
                 join(Puppy, Puppy.shelter_id == Shelter.id).\
                 order_by(Shelter.name).\
                 all()

for item in counts:
    title = '{shelter} ({cnt})'.format(shelter=item[0].name, cnt=item[1])
    print title
    print '=' * len(title)
    for r in result:
        if r[0].id == item[0].id:
            print '\t%s' % r[1].name
    print
