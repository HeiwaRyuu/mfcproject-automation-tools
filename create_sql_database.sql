-- THIS IS A BLUEPRINT FOR CREATING THE DATABASE IN SQL SERVER FOR MY APP
-- CREATE A DATABASE NAMED automation_main_db

CREATE DATABASE automation_main_db
GO

-- CREATE A TABLE NAMED urls_table WITH 2 COLUMNS (url_id, url)
CREATE TABLE urls_table (
    url_id INT IDENTITY(1,1) PRIMARY KEY,
    url VARCHAR(255) NOT NULL
)

-- CREATE A TABLE NAMED local_paths_table WITH 2 COLUMNS (local_path_id, local_path)
CREATE TABLE local_paths_table (
    local_path_id INT IDENTITY(1,1) PRIMARY KEY,
    local_path VARCHAR(255) NOT NULL
)


-- CREATE A QUERY THAT DELETES DUPLICATES IN THE TABLES (urls_table, local_paths_table)
WITH CTE AS( 
    SELECT url, ROW_NUMBER() OVER(PARTITION BY url ORDER BY url) AS RN 
    FROM urls_table
)
DELETE FROM CTE WHERE RN > 1


WITH CTE AS( 
        SELECT [local_path], ROW_NUMBER() OVER(PARTITION BY local_path ORDER BY local_path) AS RN 
        FROM [local_paths_table]
        )
        DELETE FROM CTE WHERE RN > 1
