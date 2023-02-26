#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()


# Inheritance from a declarative_base object
# data model
class Student(Base):
    
    # class attribute, used as the name of SQL db table
    __tablename__ = "students"

    # class attributes
    id = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':
    engine = create_engine("sqlite:///students.db")
    Base.metadata.create_all(engine)



# run chmod +x lib/sqlalchemy_sandbox.py to maje the script executable
# run lib/sqlalchemy_sandbox.py python shell to create db with students table

