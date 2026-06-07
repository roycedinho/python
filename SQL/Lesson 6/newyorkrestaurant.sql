-- create restaurant table
CREATE TABLE IF NOT EXISTS Restaurant (
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);

-- insert data
INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health) VALUES
('The Modern', 'Lagos', 'French', 4.5, '₦₦₦', 'A'),
('Le Bernardin', 'Lagos', 'French', 4.7, '₦₦₦₦', 'B'),
('Eleven Madison Park', 'Lagos', 'American', 4.6, '₦₦₦₦', 'A'),
('Per Se', 'Ikeja', 'American', 4.5, '₦₦₦₦', 'B'),
('Marea', 'Ikeja', 'Italian', 4.4, '₦₦₦', 'A'),
('Carbone', 'Ikeja', 'Italian', 4.3, '₦₦₦', 'B'),
('Masa', 'Ikeja', 'Japanese', 4.8, '₦₦₦₦₦', 'A'),
('Sushi Nakazawa', 'Ikeja', 'Japanese', 4.7, '₦₦₦₦', ''),
('Nobu', 'Victoria Island', 'Japanese', 4.6, '₦₦₦₦', ''),
('Casa do Saulo', 'Victoria Island', 'Brazilian', 4.5, '₦₦₦', ''),
('Marius Degustare', 'Victoria Island', 'Brazilian', 4.7, '₦₦₦₦', 'A'),
('Boka', 'Lagos', 'American', 4.4, '₦₦₦', 'A'); 

-- 1) distinct neighborhoods
SELECT DISTINCT neighborhood
FROM Restaurant;

-- 2) distinct cuisine types
SELECT DISTINCT cuisine
FROM Restaurant;

-- 3) italian takeout options
SELECT *
FROM Restaurant
WHERE cuisine = 'Italian'; 

-- 4) restaurants with review 4 and above
SELECT *
FROM Restaurant
WHERE review >= 4.0;

-- 5) japanese restaurants with ₦₦ TO ₦₦₦
SELECT *
FROM Restaurant
WHERE cuisine = 'Japanese'
  AND price IN ('₦₦', '₦₦₦');

-- 6) restaurants with exactly ₦₦₦
SELECT *
FROM Restaurant
WHERE price = '₦₦₦';

-- 7) restaurants name containing 'Masa'   
SELECT *
FROM Restaurant
WHERE name LIKE '%Masa%';

-- 8) restaurants in lagos, ikeja, or victoria island
SELECT *
FROM Restaurant
WHERE neighborhood IN ('Lagos', 'Ikeja', 'Victoria Island');

-- 9) health grade pending (empty value or NULL)
SELECT *
FROM Restaurant
WHERE health = '' OR health IS NULL;
-- 10) top 4 restaurants based on reviews
SELECT *
FROM Restaurant
ORDER BY review DESC
LIMIT 4;