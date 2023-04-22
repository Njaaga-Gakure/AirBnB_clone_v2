-- create a database named hbnb_test_db
-- create user named hbnb_test
-- grant all privileges to the above user
--  on the created database
-- grant SELECT privileges to the user
--  on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
