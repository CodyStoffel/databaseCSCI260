import psycopg2

connection = psycopg2.connect(database="csci260", user="csci260", password = "password", host = "localhost")
cursor = connection.cursor()
cursor.execute("SELECT * from test;") #Fetch all rows from database
record = cursor.fetchall()
print("Data from Database:- ", record)
