from sql_connect import connect_to_sql

## FILE FOR AUXILIAR FUNCTIONS FOR SQL SERVER DATABASE
def delete_duplicates_in_urls_table(conn, cursor):
    query = """
        WITH CTE AS( 
        SELECT [url], ROW_NUMBER() OVER(PARTITION BY url ORDER BY url) AS RN 
        FROM [urls_table]
        )
        DELETE FROM CTE WHERE RN > 1
    """
    cursor.execute(query)
    conn.commit()


def delete_duplicates_in_local_paths_table(conn, cursor):
    query = """
        WITH CTE AS( 
        SELECT [local_path], ROW_NUMBER() OVER(PARTITION BY local_path ORDER BY local_path) AS RN 
        FROM [local_paths_table]
        )
        DELETE FROM CTE WHERE RN > 1
    """
    cursor.execute(query)
    conn.commit()


def fetch_urls_from_urls_table():
    """
    Fetches all urls from the urls_table
    """
    conn, cursor = connect_to_sql()
    query = """
        SELECT url FROM urls_table
    """
    cursor.execute(query)
    urls = cursor.fetchall()
    conn.close()

    urls = [url[0] for url in urls]

    return urls


def fetch_local_paths_from_local_paths_table():
    """
    Fetches all local_paths from the local_paths_table
    """
    conn, cursor = connect_to_sql()
    query = """
        SELECT local_path FROM local_paths_table
    """
    cursor.execute(query)
    local_paths = cursor.fetchall()
    conn.close()

    local_paths = [local_path[0] for local_path in local_paths]

    return local_paths