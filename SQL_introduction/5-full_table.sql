-- Create a table named 'first_table' with specific column definitions and constraints
CREATE TABLE first_table
(
	-- Unique identifier, auto-incremented and cannot be null
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	-- A string column with a max length of 128 characters
	name VARCHAR(128),
	-- A single-character column
	c CHAR(1),
	-- A column to store date values
	created_at DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; -- Use the InnoDB storage engine (supports transactions, foreign keys, etc.)
																	-- Use utf8mb4 character set (supports full Unicode, including emojis)
																	-- Set collation for case-insensitive, accent-insensitive comparisons


-- Retrieve metadata about the columns in 'first_table' located in the 'hbtn_0c_0' database
-- This includes names, types, nullability, default values, etc.
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_0c_0'
