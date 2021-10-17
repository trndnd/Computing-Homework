import sqlite3,os

db = sqlite3.connect("Movies.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE Movies(Movie_Name text,release_Date text,genre text,rating text)")
db.commit()
db.close()
print("Database \"Movies\" has been created!")