from datetime import date

from ..entities import Actor, Movie, ContactDetail, Stunt

from model import base

# generate or migrate schema
base.Base.metadata.create_all(base.engine)

# Create a new session
session = base.Session()


# CREATE MIGRATION DATA

# Movies
bourne_identity = Movie("The bourne Identity", date(2002, 10, 11))
harry_potter_2 = Movie(
    "Harry Potter and The Chamber of Secrets", date(2002, 10, 11))


# Actors
matt = Actor("Matt Damon", date(1968, 10, 11))
daniel = Actor("Daniel Radcliff", date(1989, 10, 11))
emma = Actor("Emma Watson", date(1989, 10, 11))

# Actors to movies
bourne_identity.actors = [matt]
harry_potter_2.actors = [daniel]
harry_potter_2.actors = [emma]

#


# Insert data
session.add(bourne_identity)
session.add(harry_potter_2)

session.add(matt)
session.add(daniel)
session.add(emma)


# Save and Close
session.commit()
session.close()
