
# PostGres Server 
# psql ^    ^
#           | 
# psycopg2 +
# python3

from db import *

def deleteCourse(classDept, classNum):
    cursor = connectDB()
    query="delete from courses where class='%s' and number='%s'" %(classDept,classNum)
    print(query)
    cursor.execute(query)
    disconnectDB()

def Delete():
    print("Deleting a class from the offered classes")
    classDept=input("Please enter the class Department:")
    classNum=input("Please enter the class Number:")
    deleteCourse(classDept, classNum)

    #Use Fstring Formatted String to add class and number to query

if __name__ == "__main__":
    Delete()
    