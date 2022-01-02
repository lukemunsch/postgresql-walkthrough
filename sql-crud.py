from sqlalchemy import (
    create_engine, Float, Integer, String, ForeignKey, Column
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#  exectuing the instruction from our chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()





# instad of connecting directly to our database, we will ask for a session
# create a new instance of sessionmaker, then point to our engine - db
Session = sessionmaker(db)
# open adn actual session by calling the Session() subclass defined above
session = Session()

# create database using the  declariative_base subclass
base.metadata.create_all(db)
