-- Create the database 'hbtn_0d_2' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' restricted to local connections, if not already present
-- Set the password to 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privileges on all tables of the 'hbtn_0d_2' database to this user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
