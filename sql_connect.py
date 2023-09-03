from mysql.connector import connect, Error
from dotenv import load_dotenv
import os
import pyodbc 

load_dotenv()

def connect_to_sql_no_database(server=os.getenv("SQL_SERVER"), username=os.getenv("SQL_LOGIN"), password=os.getenv("SQL_PASSWORD")):
    """
    Connects to a SQL database using pyodbc and returns the connection and cursor objects
    """
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};UID={username};PWD={password}'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    return conn, cursor


def connect_to_sql(server=os.getenv("SQL_SERVER"), database='automation_main_db', username=os.getenv("SQL_LOGIN"), password=os.getenv("SQL_PASSWORD")):
    """
    Connects to a SQL database using pyodbc and returns the connection and cursor objects
    """
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    return conn, cursor