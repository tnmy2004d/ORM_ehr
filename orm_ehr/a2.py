import sqlite3

def display_tables(database_file):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        conn.close()

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")

database_file = 'C:\Users\tanma\OneDrive\Desktop\EHR\sampEHR.db'

display_tables(database_file)


