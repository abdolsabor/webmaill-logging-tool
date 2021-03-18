import sqlite3
#sqlite3.connect('logs.db')


def showlogs():
    try:
        sqliteConnection = sqlite3.connect('logs.db')
        cursor = sqliteConnection.cursor()
        print("Connected to Logs.db")

        sqlite_select_query = """SELECT * from Mallogs"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Email Service: ", row[1])
            print("EmailMessage: ", row[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")





conn = sqlite3.connect('logs.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

#Create table - Logs
#c.execute('''CREATE TABLE Mallogs
#             ([generated_id] INTEGER PRIMARY KEY,[WebMailused] text, [MailSent] text)''')
          




conn.commit()
print("Table created")



def WritetoLogs():
    try:
        sqliteConnection = sqlite3.connect('logs.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Mallogs
                              (WebMailused, MailSent) 
                               VALUES 
                              ('protonmail','lkcjocjsdoj')"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into Mallogs table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")




def main():
    WritetoLogs()
    showlogs()

if __name__== "__main__":
  main()




