import psycopg2

def Show():

    conn = psycopg2.connect(database="csci260", 
                            host="localhost", 
                            user="csci260", 
                            password="password")

    cursor = conn.cursor()


    query =f"select * from courses"

    for row in query:
        print(row[0],"|", row[1], "|", row[2])

    print(query)
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Show()
