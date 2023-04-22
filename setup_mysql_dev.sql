-- create a database named hbnb_dev_db
-- create user named hbnb_dev
-- grant all privileges to the above user
--  on the created database
-- grant SELECT privileges to the user
--  on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
