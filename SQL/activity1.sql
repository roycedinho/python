CREATE TABLE supplier (
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS INTEGER,
CITY TEXT
);

INSERT INTO supplier VALUES 
('S1', 'Stephon', 21, 'Georgia'),
('S2', 'Ahmed', 33, 'Lagos'),
('S3', 'Cole', 12, 'New York'),
('S4', 'Shai', 24, 'Toronto'),
('S5', 'Victor', 23, 'Le Chesnay');

SELECT * FROM supplier;