import sqlite3
class Reading:
    def __init__(self):
        self.db = sqlite3.connect("Movies.db")
        self.cursor = self.db.cursor()
        Reading.Deciding_Between_Getting_All_Data_Or_Only_Getting_Some(self)

    def Deciding_Between_Getting_All_Data_Or_Only_Getting_Some(self):
        print("Do you want to get all the data(1) or only some data(2)?")
        Answer = int(input())
        if Answer == 1:
            Reading.ReadingAllData(self)
        elif Answer == 2:
            Reading.Reading_Data_With_Conditions(self)
        else:
            print("Pick a valid optoion next time")
    
    def Reading_Data_With_Conditions(self):
        print("What do you want to condition with? Movie Name(1),Date Released(2), Genre(3) and rating(4)")
        Decision = int(input())
        if Decision == 1:
            print("What is the movie name? ")
            Movie_Name = input()
            self.cursor.execute(f"SELECT * FROM Movies WHERE Movie_Name == \"{Movie_Name}\"")
        elif Decision == 2:
            print("When was it released? ")
            Release_Date = input()
            self.cursor.execute(f"SELECT * FROM Movies WHERE release_Date == \"{Release_Date}\"")
        elif Decision == 3:
            print("What type of genre is it? ")
            Genre = input()
            self.cursor.execute(f"SELECT * FROM Movies WHERE genre == \"{Genre}\"")
        elif Decision == 4:
            print("What rating was it out of ten?")
            Rating = int(input())
            print("Would you like greater than(1),less than(2) or equal too(3)")
            Rating_Decision = int(input())
            if Rating_Decision == 1:
                self.cursor.execute(f"SELECT * FROM Movies WHERE rating > {Rating}")
            elif Rating_Decision == 2:
                self.cursor.execute(f"SELECT * FROM Movies WHERE rating < {Rating}")
            elif Rating_Decision == 3:
                self.cursor.execute(f"SELECT * FROM Movies WHERE rating == {Rating}")
        else:
            print("Actually input a correct valid next time! ")
        Data = self.cursor.fetchall()
        if Data == []:
            print("There is no data for that movie!")
        else:
            for record in Data:
                print(f"Movie name: {record[0]} Date released: {record[1]} genre: {record[2]} rating: {record[3]}/10")
        

    def ReadingAllData(self):
        self.cursor.execute(f"SELECT * FROM Movies")
        data = self.cursor.fetchall()
        for record in data:
            print(f"Movie name: {record[0]} Date released: {record[1]} genre: {record[2]} rating: {record[3]}/10")