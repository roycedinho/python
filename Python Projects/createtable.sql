CREATE TABLE Animals (
ID INT PRIMARY KEY,
Species TEXT,
Colour TEXT,
Size_cm REAL
);
INSERT INTO Animals (ID, Species, Colour, Size_cm) VALUES
(1, 'Dog', 'Brown', 50.0),
(2, 'Ostrich', 'Dark Brown', 200.0),
(3, 'Cat', 'Black', 30.0),
(4, 'Elephant', 'Grey', 300.0),
(5, 'Giraffe', 'Yellow', 500.0);

SELECT * FROM Animals;

SELECT Species, Size_cm
FROM Animals
WHERE Size_cm > 75.0;
