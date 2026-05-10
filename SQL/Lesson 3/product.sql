-- Create the PRODUCT table if it does not exist
CREATE TABLE IF NOT EXISTS PRODUCT (
    PRODUCT_ID TEXT,
    PRODUCT_NAME TEXT,
    SUPPLIER_ID TEXT,
    CATEGORY_ID TEXT,
    UNIT TEXT,    
    PRICE REAL
);

-- Insert sample data into the PRODUCT table
INSERT INTO PRODUCT (PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT, PRICE) 
VALUES
('1', 'Finley', '1', '1', '10 boxes x 20 bags', 18.00),
('2', 'Jacob', '1', '1', '24 - 12 oz bottles', 19.00),
('3', 'Andrew Savva', '1', '2', '12 - 550 ml bottles', 10.00),
('4', 'Chef Chunkz''s Cajun Seasoning', '2', '2', '48 - 6 oz jars', 22.00),
('5', 'Chef Anton''s Gumbo Mix', '2', '2', '36 boxes', 21.35);

-- Query to count the number of products
SELECT COUNT(PRODUCT_ID) AS PRODUCT_COUNT
FROM PRODUCT;

-- Query to calculate the average price
SELECT AVG(PRICE) AS AVERAGE_PRICE
FROM PRODUCT;

-- Query to find the total price
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM PRODUCT;