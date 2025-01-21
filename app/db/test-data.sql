USE msgs;

INSERT INTO authors (name) VALUES
('user1'),
('user2'),
('user3');

INSERT INTO posts (author_id, message) VALUES
(1, 'message1'),
(2, 'message2'),
(3, 'message3');
