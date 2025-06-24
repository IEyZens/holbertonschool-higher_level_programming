-- Create the table 'unique_id' only if it doesn't already exist
-- It contains:
--   - 'id': an integer with a default value of 1 and a UNIQUE constraint
--   - 'name': a variable-length string up to 256 characters
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
