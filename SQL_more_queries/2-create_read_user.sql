-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 will have only SELECT privilege on hbtn_0d_2
-- The user password will be set to user_0d_2_pwd
-- If the database or user already exists, the script will not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Revoke any existing privileges to ensure only SELECT remains
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';
REVOKE GRANT OPTION ON *.* FROM 'user_0d_2'@'localhost';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
