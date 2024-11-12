import sqlite3

DEBUG = True

# Connect to the database
conn = sqlite3.connect('orderdb.sqlite')
cursor = conn.cursor()

# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]
DEBUG and print("Tables:", tables)


# Function to get table structure
def get_table_structure(table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print(f"\nStructure for table '{table_name}':")
    for column in columns:
        col_id, name, data_type, not_null, default_value, primary_key = column
        print(f"Column ID: {col_id}, Name: {name}, Type: {data_type}, "
              f"Not Null: {not_null}, Default: {default_value}, Primary Key: {primary_key}")
    return columns

# Retrieve the structure of each table
table_structures = {}
for table in tables:
    table_structures[table] = get_table_structure(table)

DEBUG and print( table_structures)
