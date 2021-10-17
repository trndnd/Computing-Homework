import sqlite3,os

db = sqlite3.connect("Movies.db")
cursor = db.cursor()

def InsertingData():
    print("-------------------------------------------------------")
    Movie_Name = input("What is the name of the movie? ")
    print("-------------------------------------------------------")
    Date_Released = input("When was the movie released? ")
    print("-------------------------------------------------------")
    Genre = input("What type of genre is it? ")
    print("-------------------------------------------------------")
    Rating = input("What do you rate the movie out of 10? ")
    print("-------------------------------------------------------")
    cursor.execute(f"INSERT INTO Movies Values(\"{Movie_Name}\",\"{Date_Released}\",\"{Genre}\",{Rating})")
    db.commit()
    print("--------------------------")
    print("Data has been added! ")
    print("--------------------------")

def Updating():
    Field_Names = ["Movie_Name","release_Date","genre","rating"]
    Where_statment = MakingWherePartOfTheStatment()
    cursor.execute(f"SELECT * FROM Movies {Where_statment}")
    Data = cursor.fetchall()
    if Data != []:#Checks if it actually has data in it first beofre updating it
        print("-------------------------------------")
        print("Which one do you want to update?")
        print(f"1.Movie Name")
        print(f"2.Date Released")
        print(f"3.Genre")
        print(f"4.Rating")
        print("-------------------------------------")
        Answer = int(input("Choice: ")) - 1 #Avoids index errors
        print("-----------------------------------------")
        print("What would you like to change it too? ")
        print("-----------------------------------------")
        New_Data = input("New value: ")
        cursor.execute(f"UPDATE Movies SET {Field_Names[Answer]} = \"{New_Data}\" {Where_statment}")
        db.commit()
        print("-----------------------------")
        print("Data has been updated! ")
        print("-----------------------------")
    else:
        print("-------------------------------------")
        print("There is no data on that movie! ")
        print("-------------------------------------")

def Conditioning_Data():
    Where_Statment = MakingWherePartOfTheStatment()
    cursor.execute(f"SELECT * FROM Movies {Where_Statment}")
    Data = cursor.fetchall()
    if Data != []:
        for Record in Data:
            print("---------------------------")
            print(f"1.Movie Name:{Record[0]}")
            print(f"Date Released:{Record[1]}")
            print(f"Genre:{Record[2]}")
            print(f"Rating:{Record[3]}")
            print("---------------------------")
    else:
        print("------------------------------------------")
        print("There is no data with those conditions!")
        print("------------------------------------------")

def MakingWherePartOfTheStatment():
    Finished = False
    Conditions_Dictionary = {}
    while Finished == False:
        print("--------------------------------------")
        print("What do you want to condition on? ")
        print("1.Movie_Name")
        print("2.Date Released")
        print("3.Genre")
        print("4.Rating out of 10")
        print("--------------------------------------")
        Condition_field = int(input("Choice: ")) - 1
        if Condition_field not in Conditions_Dictionary and 0 <= Condition_field <= 3:
            print("--------------------------")
            print("What is the condition? ")
            print("--------------------------")
            Condition_Value = input("Condition: ")
            Conditions_Dictionary[Condition_field] = Condition_Value
            '''Adding the index value of the field name in Field_Names = ["Movie_Name","release_Date","genre","rating"] 
            with its correspding conditionm like 1:"29/10/21". The 1 is coresponds to the string 'release_Date' in the Field_Names list and the "29/10/21" is the condition or
            the moive released
            '''
        else:
            print("------------------------------------------------------------------------")
            print("You can pick this as either you already picked it or it's not valid ")
            print("------------------------------------------------------------------------")
        print("-------------------------------------------------------")
        print("Do you want to chose another condition (yes or no)")
        print("-------------------------------------------------------")
        Answer = input("Choice: ")
        if Answer.title() == "No":
            Finished = True

    #This si the part where it actually makes the where string statment
    Where_Statment = "WHERE"
    Field_Names = ["Movie_Name","release_Date","genre","rating"]
    for key in Conditions_Dictionary:
        Where_Statment += f" {Field_Names[key]} == \"{Conditions_Dictionary[key]}\" AND"
    Where_Statment = Where_Statment[:len(Where_Statment) - 4]#Gets rid of the AND at the end as if t was kept their then it would cause errors.
    return Where_Statment

def Deciding_Between_Getting_All_Data_Or_Only_Getting_Some():
    print("-----------------------------------")
    print("1.All Data")
    print("2.Filter out data via conditionns")
    print("-----------------------------------")
    Answer = int(input("Choice: "))
    if Answer == 1:
        ReadingAllData()
    elif Answer == 2:
        Conditioning_Data()
    else:
        print("----------------------------------")
        print("Pick a valid option next time")
        print("----------------------------------")

def ReadingAllData():
        cursor.execute(f"SELECT * FROM Movies")
        data = cursor.fetchall()
        if data != []:
            for record in data:
                print("-----------------------------")
                print(f"Movie Name:{record[0]}")
                print(f"Date released:{record[1]}")
                print(f"Genre:{record[2]}")
                print(f"Rating:{record[3]}")
                print("-----------------------------")
        else:
            print("---------------------------------------")
            print("There is no data in the database!")
            print("---------------------------------------")

def DeletingData():
    WhereStatment = MakingWherePartOfTheStatment()
    cursor.execute(f"SELECT * FROM Movies {WhereStatment}")
    Data = cursor.fetchall()
    if Data != []:#Checks if the data being deleted actually exists
        cursor.execute(f"DELETE FROM Movies {WhereStatment}")
        db.commit()
        print("---------------------------")
        print("Data has been deleted!")
        print("---------------------------")
    else:
        print("----------------------------------")
        print("There is no data on this moive")
        print("----------------------------------")

def Decision():
    stop = False
    while stop == False:
        print("---------Menu---------")
        print("1.Read Data")
        print("2.Adding Data")
        print("3.Updating Data")
        print("4.Deleting Data")
        print("----------------------")
        Decision = int(input("Choice: "))
        if Decision == 1:
            Deciding_Between_Getting_All_Data_Or_Only_Getting_Some()
        elif Decision == 2:
            InsertingData()
        elif Decision == 3:
            Updating()
        elif Decision == 4:
            DeletingData()
        else:
            print("---------------------------------------")
            print("Pick a vaild option next time! ")
            print("---------------------------------------")
        print("-------------------------------------------")
        print("Do you want this to end? (yes or no) ")
        print("-------------------------------------------")
        Answer = input()
        if Answer.title() == "Yes":
            stop = True

Decision()
