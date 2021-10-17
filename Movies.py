import sqlite3,os

db = sqlite3.connect("Movies.db")
cursor = db.cursor()

if not os.path.isfile("Movies.db"):
    db = sqlite3.connect("Movies.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE Movies(Movie_Name text,release_Date text,genre text,rating text)")
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

def Updating():
    Field_Names = ["Movie_Name","release_Date","genre","rating"]
    Where_statment = MakingWherePartOfTheStatment()
    print("Which one do you want to update?")
    print(f"1.Movie Name")
    print(f"2.Date Released")
    print(f"3.Genre")
    print(f"4.Rating")
    Answer = int(input()) - 1 #Avoids index errors
    print("What would you like to change it too? ")
    New_Data = input()
    cursor.execute(f"UPDATE Movies SET {Field_Names[Answer]} = \"{New_Data}\" {Where_statment}")
    db.commit()
    print("Data has been updated! ")

def Conditioning_Data():
    Where_Statment = MakingWherePartOfTheStatment()
    cursor.execute(f"SELECT * FROM Movies {Where_Statment}")
    Data = cursor.fetchall()
    if Data != []:
        for Record in Data:
            print(f"1.Movie Name:{Record[0]}")
            print(f"Date Released:{Record[1]}")
            print(f"Genre:{Record[2]}")
            print(f"Rating:{Record[3]}")
    else:
        print("There is no data with those conditions!")

def MakingWherePartOfTheStatment():
    Finished = False
    Conditions_Dictionary = {}
    while Finished == False:
        print("What do you want to condition on? ")
        print("1.Movie_Name")
        print("2.Date Released")
        print("3.Genre")
        print("4.Rating out of 10")
        Condition_field = int(input()) - 1
        if Condition_field not in Conditions_Dictionary and 0 <= Condition_field <= 3:
            print("What is the condition? ")
            Condition_Value = input()
            Conditions_Dictionary[Condition_field] = Condition_Value
        else:
            print("You can pick this as either you already picked it or it's not valid ")
        print("Do you want to chose another condition (yes or no)")
        Answer = input()
        if Answer.title() == "No":
            Finished = True
    Where_Statment = "WHERE"
    Field_Names = ["Movie_Name","release_Date","genre","rating"]
    for key in Conditions_Dictionary:
        Where_Statment += f" {Field_Names[key]} == \"{Conditions_Dictionary[key]}\" AND"
    Where_Statment = Where_Statment[:len(Where_Statment) - 4]#Gets rid of the AND at the end as if t was kept their then it would cause errors.
    return Where_Statment

def Deciding_Between_Getting_All_Data_Or_Only_Getting_Some():
    print("1.All Data")
    print("2.Filter out data via conditionns")
    Answer = int(input())
    if Answer == 1:
        ReadingAllData()
    elif Answer == 2:
        Conditioning_Data()
    else:
        print("Pick a valid option next time")

def ReadingAllData():
        cursor.execute(f"SELECT * FROM Movies")
        data = cursor.fetchall()
        for record in data:
            print(f"Date released:{record[1]}")
            print(f"Genre:{record[2]}")
            print(f"Rating:{record[3]}")

def DeletingData():
    WhereStatment = MakingWherePartOfTheStatment()
    cursor.execute(f"DELETE FROM Movies {WhereStatment}")
    db.commit()

def Decision():
    stop = False
    while stop == False:
        print("1.Read Data")
        print("2.Adding Data")
        print("3.Updating Data")
        print("4.Deleting Data")
        Decision = int(input())
        if Decision == 1:
            Deciding_Between_Getting_All_Data_Or_Only_Getting_Some()
        elif Decision == 2:
            InsertingData()
        elif Decision == 3:
            Updating()
        elif Decision == 4:
            DeletingData()
        else:
            print("Pick a vaild option! ")
        print("Do you want this to end? ")
        Answer = input()
        if Answer.title() == "Yes":
            stop = True

Decision()
