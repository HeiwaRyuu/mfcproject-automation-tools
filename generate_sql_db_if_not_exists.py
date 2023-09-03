from sql_connect import connect_to_sql_no_database

def create_database():
    """
    Creates the database in SQL Server IF NOT EXISTS
    """
    conn, cursor = connect_to_sql_no_database()
    conn.autocommit = True ## VERY IMPORTANT SETTING, OTHERWISE IT WILL NOT RUN
    create_database_query = "IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'automation_main_db') BEGIN CREATE DATABASE automation_main_db END"
    cursor.execute(create_database_query)
    print("Database created successfully")
    conn.commit()
    conn.close()

def create_tables():
    """
    Creates the tables in the database IF NOT EXISTS
    """
    conn, cursor = connect_to_sql_no_database()
    cursor.execute('''
    USE automation_main_db
    IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'urls_table')
    BEGIN
        CREATE TABLE urls_table (
            url_id INT IDENTITY(1,1) PRIMARY KEY,
            url VARCHAR(255) NOT NULL
        )
    END
    ''')
    print("URLs table created successfully")

    cursor.execute('''
    USE automation_main_db
    IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'local_paths_table')
    BEGIN
        CREATE TABLE local_paths_table (
            local_path_id INT IDENTITY(1,1) PRIMARY KEY,
            local_path VARCHAR(255) NOT NULL
        )
    END
    ''')
    print("Local paths table created successfully")

    conn.commit()
    conn.close()