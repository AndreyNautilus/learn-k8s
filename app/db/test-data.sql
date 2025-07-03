USE msgs;

INSERT INTO authors (name) VALUES
('Selira Moonshade'),
('Kaelric Thornspire'),
('Elowen Starbreeze');

INSERT INTO posts (add_timestamp, author_id, message) VALUES
(
    current_timestamp() - 1,
    1,
    'No matter your troubles, there is always a seat, a smile, '
    'and the finest ale this side of the realm waiting at my tavern.'
),
(
    current_timestamp() - 2,
    2,
    'If the game lets me raid, pillage, and crush my foes beneath my axe, '
    'then it''s a game worthy of my time!'
),
(
    current_timestamp() - 3,
    3,
    'The sea calls louder than any landbound game - but if it''s got ships '
    'and storms, you''ll find me at the helm!'
);
