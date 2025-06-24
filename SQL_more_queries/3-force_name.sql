-- Create the table 'force_name' only if it doesn't already exist
-- It contains:
--   - 'id': an integer (nullable by default)
--   - 'name': a string (max 256 characters) that must not be NULL
CREATE TABLE IF NOT EXISTS force_name
(
	id INT,
	name VARCHAR(256) NOT NULL
);
