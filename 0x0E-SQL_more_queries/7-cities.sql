-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table cities in hbtn_0d_usa if it does not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
