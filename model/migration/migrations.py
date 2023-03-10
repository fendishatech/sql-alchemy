import datetime

from model import actor, contact_details, movie, stuntman

from model import base

# generate or migrate schema
base.Base.metadata.create_all(base.engine)
