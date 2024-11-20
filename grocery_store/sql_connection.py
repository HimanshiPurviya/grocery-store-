import mysql.connector

# Global variable to hold the connection
_cnx = None

def get_sql_connection():
    """
    Establishes and returns a MySQL database connection.
    Uses a global variable to ensure a single connection is reused.
    """
    global _cnx  # Declare that we're modifying the global variable
    if _cnx is None:  # Check if connection is already established
        print("Opening MySQL connection")
        _cnx = mysql.connector.connect(
            user='root',
            password='020604',
            database='grocery_store'
        )
    return _cnx