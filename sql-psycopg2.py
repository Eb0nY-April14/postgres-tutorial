# HOW TO EXECUTE SIX QUERIES USING THE POPULAR "psycopg2" LIBRARY.

import psycopg2


# We need to have psycopg2 connect to our Postgres database
# called chinook using the .connect() method, and we'll assign
# that to a variable of 'connection'.
# We specified the name of our database, "chinook", in double
# -quotes, but we can include additional connection values such
# as host, username, password etc.
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database. The connection needs an
# instance of a Cursor Object. A cursor object is another way of
# saying a 'set' or 'list', similar to an 'array' in JavaScript.
# Essentially, anything that we query from the database will become
# part of this cursor object and to read that data, we should iterate
# over the cursor using for e.g a for-loop.
cursor = connection.cursor()

# In between when our cursor variable being defined & our results fetched,
# we need to perform our queries using the .execute() method.
# Query 1 - Select ALL records from the "Artist" table.
# It's extremely important to note that we absolutely must use single-quotes
# to wrap our query and double-quotes to specify particular values as done
# below.
cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table.
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only the "Queen" from the "Artist" table.
# NOTE: Since we need to specify a particular record, any combination of
# single or double quotes just won't work. We need to use a Python string
# placeholder & then define the desired string within a list.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# NOTE THAT:
# We can have multiple placeholders depending on how detailed your query
# needs to be & each placeholder would be added to this list as shown
# below but commented out.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s, %s, %s', ["Queen,
#  Jane, Lucy"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table.
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from the "Track"
# table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - Select all tracks where the composer is "Robert Johnson" from the
# "Track" table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" =
# %s', ["Robert Johnson"])

# Query 8 - Select all tracks where the composer is "test" from the
# "Track" table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Query 9 - Select ALL where the "Composer" is "Robert Johnson" from the
# "Track" table.
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" =
# %s', ["Robert Johnson"])

# Query 10 - Select "Price" where the "Composer" is "Robert Johnson" from the
# "Track" table.
# cursor.execute('SELECT * FROM "Album" WHERE "Unit Price" = %s',
# [0.99])

# Query 11 - Select ALL from the "Album" table.
# cursor.execute('SELECT * FROM "Album"')

# fetch the results (multiple). We need to set up a way for our data
# to be retrieved or fetched from the cursor before we can start to
# query the database. We'll  assign this fetched data to a variable
# of 'results' since it'll fetch any result that gets queried.
# To query multiple records from our database, we should use the
# ".fetchall()" method otherwise, if we're intentionally looking
# for one particular record, we could use the ".fetchone()" method.
# fetch the results (multiple):
results = cursor.fetchall()

# fetch the result (single):
# results = cursor.fetchone()

# Close the connection i.e end the connection to the database so the
# connection is not always persistent.
connection.close()

# Since our data sits within a cursor object, similar to an array, in
# order to retrieve each record individually, we need to iterate over
# the results using a for-loop i.e For each individual result in the
# results list, print the result.
for result in results:
    print(result)

# command to type at the terminal in order to run our code is:
# python3 sql-psycopg2.py
