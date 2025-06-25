-- Create the database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the table 'cities' only if it doesn't already exist
-- The table includes:
--   - 'id': primary key, auto-incremented, not null
--   - 'state_id': foreign key that references 'states(id)', not null
--   - 'name': a string (up to 256 characters), not null
CREATE TABLE IF NOT EXISTS cities
(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
