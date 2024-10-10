
# PostGres Server 
# psql ^    ^
#           | 
# psycopg2 +
# python3

import psycopg2

def ShowStr():
    conn = psycopg2.connect(database="csci260",
                            host="localhost",
                            user="csci260",
                            password="password")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")

    data=cursor.fetchall()

    #print(data)
    returnValue=''
    for row in data:
        returnValue=returnValue+"%s|%s|%s\n"%(row[0],row[1],row[2])
    cursor.close()
    conn.close()
    return returnValue

def Show():
    print(ShowStr())

if __name__ == "__main__":
    Show()
