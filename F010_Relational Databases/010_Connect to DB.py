import sqlite3

def main():
    # Specify the database file path
    db_path = "orderdb.sqlite"  
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        print("Connected to the database successfully.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
