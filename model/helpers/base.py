# coding = utf-8
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = "mdb.db"
db_path = f"{os.getcwd()}\\{db_name}"

db_uri = f"sqlite:///{db_path}"

engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)


Base = declarative_base()
