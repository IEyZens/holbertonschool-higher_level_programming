-- Create the table 'id_not_null' only if it doesn't already exist
-- It contains:
--   - 'id': an integer that defaults to 1 if no value is provided (but still allows NULL explicitly)
--   - 'name': a variable-length string up to 256 characters
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
