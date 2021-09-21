# HOW TO PERFORM 'CR' OF CRUD FUNCTIONALITY USING THE "SQLAlchemy" ORM.

from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db.
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create a class-based model for the "Programmer" table.
class Programmer(base):
    # The __tablename__ will match the class itself, "Programmer".
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for
# a session.
# creates a new instance of sessionmaker & point to our'db' engine
# variable in order to use the database.
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined
# above.
session = Session()

# creating the database using declarative_base subclass.
base.metadata.create_all(db)


# creating records on our Programmer table.
# For each new record we add, we'll assign
# it to a variable using the programmer's
# name as the actual variable.
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="British",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

christiana_temiola = Programmer(
    first_name="Christiana",
    last_name="Temiola",
    gender="F",
    nationality="Irish",
    famous_for="Python ORM Language"
)

# Add her to the table by using our current session
# and then commit that session.
# One good thing about using the ORM and sessions, is
# that the formatting for adding records is quite similar
# to using Git when pushing files to GitHub.
# add each instance of our programmers to our session.
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(christiana_temiola)


# updating a single record.
# Since we only want one specific record, we must add the
# .first() method at the end of our query or else we'll
# have to use a for-loop to iterate over the query list,
# even though it'll only find a single record using that ID.
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# # commit our session to the database.
# session.commit()

# updating multiple records.
# update everybody's record at the same time so we need to
# iterate over each record using a for-loop.
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print(
#         "Programmer Found: ", programmer.first_name + " " + programmer.
#         last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n)
#         ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted!")
#     else:
#         print("Programmer not deleted!")
# else:
#     print("No records found")


# query the database to find all Programmers i.e check
# that Ada is added correctly. We'll create a new
# variable to find all 'programmers' & then use the
# session to query our Programmer table.
programmers = session.query(Programmer)
# even though we know there is only one programmer for now,
# we'll create a for-loop over this list of programmers which
# will also prepare us for having more added later.
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
