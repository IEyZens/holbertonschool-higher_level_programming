-- Create the table 'second_table' only if it doesn't already exist
-- It has three columns:
--   - 'id': an integer
--   - 'name': a string up to 256 characters
--   - 'score': an integer
CREATE TABLE second_table
(
	id INT,
	name VARCHAR(256),
	score INT
)

-- Insert four rows into 'second_table' with specified id, name, and score values
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
