import sqlite3
import time

def fetch_all_orders_and_compare_in_python(cursor):
    """Function 1: Retrieve all orders, fetch order items per order, sum in Python, and compare."""
    cursor.execute("SELECT Id, TotalAmount FROM Orders")
    orders = cursor.fetchall()
    results = []

    for order_id, total_amount in orders:
        cursor.execute("SELECT UnitPrice, Quantity FROM OrderItems WHERE OrderId = ?", (order_id,))
        order_items = cursor.fetchall()
        
        # Sum up the total of order items in Python
        item_total = sum(unit_price * quantity for unit_price, quantity in order_items)
        
        # Compare and store the result
        status = "OK" if item_total == total_amount else "Not OK"
        results.append((order_id, status))
    
    return results

def fetch_orders_with_summed_order_items(cursor):
    """Function 2: Let SQL sum the order items, then compare in Python."""
    cursor.execute("SELECT Id, TotalAmount FROM Orders")
    orders = cursor.fetchall()
    results = []

    for order_id, total_amount in orders:
        cursor.execute("SELECT SUM(UnitPrice * Quantity) FROM OrderItems WHERE OrderId = ?", (order_id,))
        item_total = cursor.fetchone()[0] or 0.0  # Default to 0 if no order items
        
        # Compare and store the result
        status = "OK" if item_total == total_amount else "Not OK"
        results.append((order_id, status))
    
    return results

def compare_totals_in_sql(cursor):
    """Function 3: Perform all comparisons in SQL and return only mismatched results."""
    cursor.execute("""
        SELECT Orders.Id,
               CASE 
                   WHEN Orders.TotalAmount = IFNULL(SUM(OrderItems.UnitPrice * OrderItems.Quantity), 0) 
                   THEN 'OK' 
                   ELSE 'Not OK' 
               END AS Status
        FROM Orders
        LEFT JOIN OrderItems ON Orders.Id = OrderItems.OrderId
        GROUP BY Orders.Id
    """)
    return cursor.fetchall()

def time_functions(cursor):
    """Time each function and report the results."""
    num_iterations = 10
    times = {}
    
    # Time Function 1
    start = time.time()
    for _ in range(num_iterations):
        fetch_all_orders_and_compare_in_python(cursor)
    times["fetch_all_orders_and_compare_in_python"] = (time.time() - start) / num_iterations
    
    # Time Function 2
    start = time.time()
    for _ in range(num_iterations):
        fetch_orders_with_summed_order_items(cursor)
    times["fetch_orders_with_summed_order_items  "] = (time.time() - start) / num_iterations
    
    # Time Function 3
    start = time.time()
    for _ in range(num_iterations):
        compare_totals_in_sql(cursor)
    times["compare_totals_in_sql                 "] = (time.time() - start) / num_iterations

    # Report the results
    for func_name, avg_time in times.items():
        print(f"{func_name} average execution time: {avg_time:.6f} seconds")

def main():
    # Specify the database file path
    db_path = "orderdb.sqlite"  

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("Connected to the database successfully.")

        # Run and time all three functions
        time_functions(cursor)
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()

