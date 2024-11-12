import sqlite3

def list_tables(cursor):
    """List all tables in the database."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    if tables:
        print("Tables:")
        for table in tables:
            print(f"  - {table[0]}")
    else:
        print("No tables found in the database.")

def execute_sql_old(cursor, sql):
    """Execute a SQL command and print the results."""
    try:
        cursor.execute(sql)
        if sql.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            if rows:
                # Print column headers
                column_names = [description[0] for description in cursor.description]
                print(" | ".join(column_names))
                print("-" * (len(column_names) * 15))
                # Print rows
                for row in rows:
                    print(" | ".join(str(value) for value in row))
            else:
                print("Query returned no results.")
        else:
            print(f"{cursor.rowcount} rows affected.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def execute_sql(cursor, sql):
    """Execute a SQL command and print the results with formatted column widths."""
    try:
        cursor.execute(sql)
        
        if sql.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            
            if rows:
                # Get column names and calculate max width for each column
                column_names = [description[0] for description in cursor.description]
                max_lengths = [len(name) for name in column_names]  # Start with column title lengths

                # Calculate max length for each column based on row data
                for row in rows:
                    for idx, value in enumerate(row):
                        max_lengths[idx] = max(max_lengths[idx], len(str(value)))

                # Print column headers
                header = " | ".join(name.ljust(max_lengths[i]) for i, name in enumerate(column_names))
                print(header)
                print("-" * len(header))

                # Print each row with adjusted column widths
                for row in rows:
                    row_str = " | ".join(str(value).ljust(max_lengths[i]) for i, value in enumerate(row))
                    print(row_str)
            else:
                print("Query returned no results.")
        else:
            print(f"{cursor.rowcount} rows affected.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    db_path = input("Enter the path to your SQLite database: ")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Connected to the database. Type '.tables' to list all tables or enter SQL commands ending with a semicolon (;). Type 'exit' to quit.")

    if False: # Old version
        print("Connected to the database. Type '.tables' to list all tables or enter SQL commands. Type 'exit' to quit.")

        while True:
            command = input("sqlite> ").strip()
            
            if command.lower() == "exit":
                print("Exiting.")
                break
            elif command == ".tables":
                list_tables(cursor)
            else:
                execute_sql(cursor, command)
                # Commit changes if it was an action query
                if command.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    conn.commit()


    sql_command = ""  # To accumulate multi-line commands

    while True:
        line = input("sqlite> ").strip()
        
        # Check for command shortcuts
        if line.lower() == "exit":
            print("Exiting.")
            break
        elif line == ".tables":
            list_tables(cursor)
            continue
        
        # Add line to the accumulated command
        sql_command += " " + line

        # If a semicolon is found at the end, execute the command
        if sql_command.strip().endswith(";"):
            # Remove the semicolon before executing
            sql_command = sql_command.strip().rstrip(";")
            execute_sql(cursor, sql_command)
            
            # Commit if it's an action query
            if sql_command.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                conn.commit()
            
            # Clear the accumulated command after execution
            sql_command = ""


    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
