import sqlite3,os
from Reading_data import Reading

db = sqlite3.connect("Movies.db")
cursor = db.cursor()

if not os.path.isfile("Movies.db"):
    db = sqlite3.connect("Movies.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE Movies(Movie_Name text,release_Date text,genre text,rating int)")
    db.commit()
    db.close()

def InsertingData():
    Movie_Name = input("What is the name of the movie? ")
    Date_Released = input("When was the movie released? ")
    Genre = input("What type of genre is it? ")
    Rating = int(input("What do you rate the movie out of 10? "))
    cursor.execute(f"INSERT INTO Movies Values(\"{Movie_Name}\",\"{Date_Released}\",\"{Genre}\",{Rating})")
    db.commit()
    print("Data has been added! ")

def Decision():
    stop = False
    while stop == False:
        print("Do you want to read(1),insert(2) or update(3) data? ")
        Decision = int(input())
        if Decision == 1:
            Reading()
        elif Decision == 2:
            InsertingData()
        elif Decision == 3:
            print()
        else:
            print("Pick a vaild option! ")
        print("Do you want this to end? ")
        Answer = input()
        if Answer.title() == "Yes":
            stop = True
#