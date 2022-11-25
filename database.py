import pyodbc

# Code for connecting to a server
# connection = pyodbc.connect("DSN=<dsn>;UID=<user>;PWD=<password>") # Connection string

def connect():
    '''connects to the database.
    TODO take an argument that is the connection string'''
    connect_string = "Driver={ODBC Driver 13 for SQL Server};Server=LAPTOP-9BQDP4LO\SQLEXPRESS;Database=foodbase;Trusted_Connection=yes;"

    connection = pyodbc.connect(connect_string)
    return connection.cursor()

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM ingredients")

# for row in cursor:
#     print(f"row = {row}")

