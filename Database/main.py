# import sqlite3
# connect_i=sqlite3.connect('college.sqlite3') #it creates the database
#
# # changeable ie insert delete and update
# cursor=connect_i.cursor()
#
# #Create table in database using cursor.execute
# #execute prepare the table
#
# def create_table():
#    try:
# #execute the sql command
#      cursor.execute("""
#    CREATE TABLE IF NOT EXISTS students(
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL,
#              email TEXT NOT NULL UNIQUE,
#              address TEXT NOT NULL
#              )
#     """)
#    connect_i.commit() #Once a commit is executed, the data is written to the disk and becomes permanent.
#  #It can't be changeable
#    print("Table created successful!")
# #Run the function
# create_table()


import sqlite3

# 1. This creates the file in the SAME folder as your python script
connect_i = sqlite3.connect('college.sqlite3')
cursor = connect_i.cursor()

def create_table():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        # CRITICAL: commit must have () to actually save!
        connect_i.commit()
        print("Success: Table 'students' created.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # 2. Always close the connection to finish writing to the file
        connect_i.close()

create_table()

def insert(name,emai,address):
    try:
        cursor.execute("""
        INSERT INTO STUDENTS(name,email,address) VALUES(?,?,?)
                       """,(name,email,address))
        connect_i.commit()
        print("table students inserted.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        connect_i.close()
name=input("Enter student name: ")
email=input("Enter student email: ")
address=input("Enter student address: ")
insert(name,email,address)