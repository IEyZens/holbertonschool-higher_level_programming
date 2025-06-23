-- Retrieve metadata about all columns in the table named 'first_table'
-- This includes column names, data types, defaults, etc.
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_0c_0'
