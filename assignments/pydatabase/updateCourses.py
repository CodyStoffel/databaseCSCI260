
# PostGres Server 
# psql ^    ^
#           | 
# psycopg2 +
# python3

from db import *


def updateCourse(classNewNum,classDept,classNum):
    cursor = connectDB()
    query="update courses set number='%s' where class='%s' and number='%s'" %(classNewNum,classDept,classNum)
    print(query)
    cursor.execute(query)
    disconnectDB()

def Update():
    
    print("Updating a class number in the offered classes")
    classDept=input("Please enter the class Department:")
    classNum=input("Please enter the class Number:")
    classNewNum=input("Please enter the new class Number:")
    updateCourse(classNewNum,classDept,classNum)
    #Use Fstring Formatted String to add class and number to query

if __name__ == "__main__":
    Update()
