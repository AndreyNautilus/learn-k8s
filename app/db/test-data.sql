USE msgs;

INSERT INTO authors (name) VALUES
('user1'),
('user2'),
('user3');

INSERT INTO posts (author_id, message) VALUES
(0, 'message1'),
(1, 'message2'),
(2, 'message3');
