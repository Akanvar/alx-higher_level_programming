-- Write a script that creates a table called first_table in the current database in your MySQL server.
-- table field are id(INT) and name(VARCHAR(256))
-- if table already exists, do nothing
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
