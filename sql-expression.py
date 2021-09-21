# HOW TO EXECUTE SIX QUERIES USING THE "SQLAlchemy" EXPRESSION LANGUAGE.


from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db.
# Next, we need to link our Python file to our Chinook database,
# and that's where the 'create_engine' component comes into play.
# We'll assign this to a variable of "db" to represent our database,
# and using create_engine, we can tell it to point to our local Chinook
# database within our Postgres server.
# The 3 slashes here signifies that our database is hosted locally within
# our workspace environment.
# This command/expression below creates the engine & connects it to our
# database.
db = create_engine("postgresql:///chinook")

# We'll use the MetaData class, which we can save to a variable name
# of 'meta'. This class will contain a collection of our table objects
# and the associated data within those objects.
# it's recursive data about data, meaning the data about our tables &
# the data about the data in those tables.
meta = MetaData(db)

# Before we start to query the database, we need to construct our
# tables for Python to know the schema that we're working with.
# Sometimes we'll hear this referred to as data models. we'll
# learn about data models later but for now, we'll perform the
# same six queries from Chinook that we've done previously.
# Our first table class/model, will be for the Artist table, which
# we'll assign to the variable of 'artist_table'. Then, using the
# Table import, we need to specify the name of our table, and
# provide the meta schema.
# Within our file, the format when defining columns is the column
# name followed by the type of data presented & then any other
# optional fields after that.
# In our case, we have a column for "ArtistId" which is an Integer
# & for this one, we can specify that primary_key is set to True.
# The next column is for "Name" & this is simply just a String with
# no other values necessary.
# create variable for "Artist" table.
# artist_table = Table(
#     "Artist", meta,
#     Column("ArtistId", Integer, primary_key=True),
#     Column("Name", String)
# )

# create variable for "Album" table.
# album_table = Table(
#     "Album", meta,
#     Column("AlbumId", Integer, primary_key=True),
#     Column("Title", String),
#     # With the ForeignKey, we need to tell it which table and
#     # key to point to so in this case, it's artist_table.ArtistId
#     # using the table defined above.
#     Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
# )

# create variable for "Track" table.
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    # MediaTypeId & GenreId are both Integers & are foreign keys
    # as well but for these lessons, we won't define all tables,
    # just those that we need so we can simply set their primary_key
    # to False
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Making the connection. We'll connect to the database using the
# .connect() method & the Python with-statement. This saves our
# connection to the database into a variable called 'connection'.
# We'll start to query the database since all three of our tables
# have been defined above as variables.
with db.connect() as connection:

    # Query 1 - Select ALL records from the "Artist" table.
    # For the sake of ease, we'll declare a variable called
    # 'select_query' & reuse it for all our defined six queries
    # but we can comment-out the ones not needed at any point in time.
    # Using the Expression Language, we'll apply the .select()
    # method onto our table.
    # select_query = artist_table.select()

    # Query 2 - Select only the "Name" column from the "Artist" table.
    # It'll be exactly the same as Query 1 above except that we'll use
    # the .with_only_columns() method.
    # NOTE: Even if we want to grab results from a single column, we need
    # to wrap the column selection inside of a list. Also, using dot-nation,
    # we need to use ".c" in our selection, which will identify a specific
    # column header on the table as done below.
    # select_query = artist_table.select().with_only_columns(
    #     [artist_table.c.Name])

    # Query 3 - Select only the "Queen" from the "Artist" table.
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # # Query 4 - Select only by "ArtistId" #51 from the "Artist" table.
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select only the albums with "ArtistId" #51 on the "Album"
    # table.
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all tracks where the composer is "Queen" from the
    # "Track" table.
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    # We'll run this query using the .execute() method from our
    # database connection & store the query results into a
    # variable called "results".
    results = connection.execute(select_query)
    # Iterate over each result found & print it to the Terminal.
    for result in results:
        print(result)
