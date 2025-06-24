-- Create the database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the 'hbtn_0d_usa' database to make it the active one
USE hbtn_0d_usa;

-- Create the table 'states' only if it doesn't already exist
-- The table includes:
--   - 'id': a unique auto-incremented integer that serves as the primary key
--   - 'name': a required string (up to 256 characters) representing the state name
CREATE TABLE IF NOT EXISTS states
(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
