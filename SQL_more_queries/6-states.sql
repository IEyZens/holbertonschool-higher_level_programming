-- Create the database 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table 'states' only if it doesn't already exist, inside the currently selected database
-- The table includes:
--   - 'id': an auto-incrementing primary key that cannot be NULL
--   - 'name': a string column (up to 256 characters) that must not be NULL
CREATE TABLE IF NOT EXISTS states
(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
