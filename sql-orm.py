# HOW TO EXECUTE SIX QUERIES USING THE "SQLAlchemy" ORM.

# We don't need to import the Table class here because with
# the ORM, we won't create tables but instead, we'll be
# creating Python classes. These Python classes that we'll
# create will subclass the declarative_base, meaning that
# any class we're making will extend from the main class
# within the ORM.
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
# instead of making a connection to the database directly,
# we'll be asking for a session.
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db.
# We'll create a new variable of 'db', and use create_engine
# to point to our specific database location. This tells the
# application that we're using the Postgres server, on a local
# host since there are 3 slashes, in order to connect to our
# Chinook database.
db = create_engine("postgresql:///chinook")

# We'll make a variable called 'base' which will be set to the
# declarative_base() class. This new 'base' class will essent-
# ially grab the metadata that is produced by our database
# table schema & create a subclass to map everything back to us
# here within the 'base' variable i.e we're piggybacking off of
# an existing ORM class & let it do all of the dirty work while
# we're reaping the benefits from it behind the scenes.
base = declarative_base()


# We'll start to build our class-based models by simply building
# a normal Python object that subclasses 'base'. We'll work with
# the same 3 tables in 'chinook' database as before i.e Artist,
# Album & Track but ensure these are added before the Session is
# created but after the base is declared since we need to use the
# base subclass.
# NOTE: For best practice, it's best to use PascalCase (i.e the
# first letter of each word is capitalized) when defining your
# classes in Python & don't use underscores.
# Create a class-based model for the "Artist" table.
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Create a class-based model for the "Album" table.
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create a class-based model for the "Track" table.
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    # If we ever confuse Float with Decimal & are in
    # doubt as to which is the right one to use, just
    # check on the SQLAlchemy documentation under the
    # section called "Column and Data Types".
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for
# a session.
# This 'Session' variable will instantiate the sessionmaker() class
# from the ORM, creates a new instance of sessionmaker & point to our
# 'db' engine variable in order to use the database.
Session = sessionmaker(db)
# To connect to the database, call Session() & open an actual session.
# To do that, we need another variable called 'session' (i.e lowercase
# 's') & set it to equal the new instance of the Session() from above.
session = Session()

# create the database subclass and generate all metadata i.e creating
# the database using declarative_base subclass.
# The base variable, since it's a subclass from the declarative_base,
# will now use the .create_all() method from our database metadata.
base.metadata.create_all(db)


# Query 1 - Select ALL records from the "Artist" table.
# We'll create a new variable called 'artists' & using our existing
# 'session' instance, we'll use the .query() method to query the
# Artist class. This selects everything on the table within the Artist
# class we defined above.
# artists = session.query(Artist)
# # We'll then iterate over the results found & print each of the columns
# # using dot-notation on our for-loop.
# for artist in artists:
#     # We'll print each of the columns & also separate each item using
#     # the Python separator & have them split using the vertical-bar
#     # or pipe with a space on either side.
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select only the "Name" column from the "Artist" table.
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select only the "Queen" from the "Artist" table.
# Since we only want to find a single artist, the new variable
# will be 'artist', singular. We can then use the .filter_by()
# method & with the 'Name' column, we'll specify "Queen". Also,
# since it should only return one record, we can use the .first()
# method to only give us the first item from the query.
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 4 - Select only by "ArtistId" #51 from the "Artist" table.
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 5 - Select only the albums with "ArtistId" #51 on the "Album"
# table.
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")


# Query 6 - Select all tracks where the composer is "Queen" from the
# "Track" table.
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
