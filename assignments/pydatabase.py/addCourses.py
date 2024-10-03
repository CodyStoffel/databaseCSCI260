import psycopg2

def Add():
    conn = psycopg2.connect(database="csci260", 
                            host="localhost", 
                            user="csci260", 
                            password="password")

    cursor = conn.cursor()

    print("Adding a class to the offered classes")
    classDep=input("Please enter the class department: ")
    classNum=input("Please enter the clas number: ")

    query =f"insert into courses (class,number) values({classDep}, {classNum})"
    print(query)
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Add()
