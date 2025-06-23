-- Create a table named 'first_table' only if it doesn't already exist
-- The table contains:
--   - 'id': an integer column
--   - 'name': a variable-length string column with a maximum of 256 characters
CREATE TABLE IF NOT EXISTS first_table
(
	id INT,
	name VARCHAR(256)
)
