USE msgs;

INSERT INTO authors (name) VALUES
('user1'),
('user2'),
('user3');

INSERT INTO posts (add_timestamp, author_id, message) VALUES
(current_timestamp() - 1, 1, 'message1'),
(current_timestamp() - 2, 2, 'message2'),
(current_timestamp() - 3, 3, 'message3');
