
# PostGres Server 
# psql ^    ^
#           | 
# psycopg2 +
# python3

import psycopg2

def Add():
    conn = psycopg2.connect(database="csci260",
                            host="localhost",
                            user="csci260",
                            password="password")

    cursor = conn.cursor()

    print("Adding a class to the offered classes")
    classDept=input("Please enter the class Department:")
    classNum=input("Please enter the class Number:")

    #Use Fstring Formatted String to add class and number to query
    query="insert into courses (class,number) values ('%s','%s');" %(classDept,classNum)
    print(query)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Add()
