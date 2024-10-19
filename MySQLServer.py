import mysql.connector

def creat_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kwame.6823"
        )
        if mydb.is_connected():
            cursor = mydb.cursor()
            create_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_query)
            print("Database 'alx_book_store' created successfully")




    except Exception as e:
        print(f"Error: {e}")


    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    creat_db()

