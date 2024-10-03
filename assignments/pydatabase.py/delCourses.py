import psycopg2

def Delete():

    conn = psycopg2.connect(database="csci260", 
                            host="localhost", 
                            user="csci260", 
                            password="password")

    cursor = conn.cursor()

    print("Deleting a class from the offered classes")
    classDep=input("Please enter the class department: ")
    classNum=input("Please enter the clas number: ")

    query =f"delete from courses where class={classDep} and number={classNum}"
    print(query)
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Delete()
