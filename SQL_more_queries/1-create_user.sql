-- Create the user 'user_0d_1' restricted to local connections ('localhost') if they do not already exist
-- Set their password to 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to 'user_0d_1' connecting from 'localhost'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
