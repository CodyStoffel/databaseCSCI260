import psycopg2

def Update():
    conn = psycopg2.connect(database="csci260", 
                            host="localhost", 
                            user="csci260", 
                            password="password")

    cursor = conn.cursor()

    print("Update a class number in the offered classes")
    classDep=input("Please enter the class department: ")
    classNum=input("Please enter the clas number: ")
    classNewNum=input("Please enter the new class number: ")

    query =f"update courses set number={classNewNum} where class={classDep} and number={classNum}"
    print(query)
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    Update()
