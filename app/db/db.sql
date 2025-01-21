CREATE DATABASE msgs;
USE msgs;

CREATE TABLE authors (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name text NOT NULL
);
CREATE TABLE posts (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    author_id int NOT NULL REFERENCES authors(id),
    message text
);

-- TODO: create users
