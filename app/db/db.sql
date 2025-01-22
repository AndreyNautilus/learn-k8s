-- 'name' is a reserved word in MySQL, but still can be used as field identifier
-- sqlfluff:rules:references.keywords:ignore_words:name

CREATE DATABASE IF NOT EXISTS msgs;
USE msgs;

CREATE TABLE IF NOT EXISTS authors (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name text NOT NULL
);
CREATE TABLE IF NOT EXISTS posts (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    author_id int NOT NULL REFERENCES authors (id),
    message text
);

-- TODO: create users
