--create database if it doesnt exists
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
--create user if it doesnt exist
CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
--grant select privilige to the user
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
