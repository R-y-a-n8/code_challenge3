-- Insert sample bands
INSERT INTO bands (name, hometown)
VALUES ('The Beatles', 'Liverpool'),
       ('Rolling Stones', 'London'),
       ('Queen', 'London');

-- Insert sample venues
INSERT INTO venues (title, city)
VALUES ('Wembley Stadium', 'London'),
       ('Madison Square Garden', 'New York'),
       ('Sydney Opera House', 'Sydney');

-- Insert sample concerts
INSERT INTO concerts (band_id, venue_id, date)
VALUES (1, 1, '1965-08-15'),  -- The Beatles at Wembley Stadium
       (2, 2, '1969-07-04'),  -- Rolling Stones at Madison Square Garden
       (3, 1, '1985-07-13'),  -- Queen at Wembley Stadium
       (2, 3, '1970-09-15');  -- Rolling Stones at Sydney Opera House
