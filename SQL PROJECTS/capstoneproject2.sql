-- ====================================================================
-- CAPSTONE PROJECT 2: MASTER SCRIPT
-- Topics: LIKE Operator, DISTINCT, Filtering, and Sorting (ORDER BY)
-- ====================================================================

-- --------------------------------------------------------------------
-- STEP 1: Database & Table Setup
-- --------------------------------------------------------------------
-- Drop the table if it already exists to start fresh
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- Insert sample records representing mixed data types for filtering
INSERT INTO products (product_id, product_name, category, price, stock_quantity) VALUES
(1, 'Wireless Deluxe Mouse', 'Electronics', 25.99, 120),
(2, 'Ergonomic Office Chair', 'Furniture', 149.50, 15),
(3, 'Bluetooth Headphones', 'Electronics', 89.99, 45),
(4, 'Gaming Mechanical Keyboard', 'Electronics', 75.00, 0),
(5, 'Leather Office Chair', 'Furniture', 199.99, 8),
(6, 'USB-C Charging Cable', 'Electronics', 12.50, 200),
(7, 'Standing Desk Converter', 'Furniture', 120.00, 22);


-- --------------------------------------------------------------------
-- STEP 2: The LIKE Operator (Pattern Matching)
-- --------------------------------------------------------------------

-- Task 2A: Match prefix (Starts with 'Wireless')
SELECT * FROM products 
WHERE product_name LIKE 'Wireless%';

-- Task 2B: Match substring (Contains 'Office' anywhere)
SELECT * FROM products 
WHERE product_name LIKE '%Office%';


-- --------------------------------------------------------------------
-- STEP 3: Filtering & Unique Values (DISTINCT)
-- --------------------------------------------------------------------

-- Task 3A: Find all unique categories in the database
SELECT DISTINCT category 
FROM products;

-- Task 3B: Find unique categories that actually have items in stock
SELECT DISTINCT category 
FROM products 
WHERE stock_quantity > 0;


-- --------------------------------------------------------------------
-- STEP 4: Mixed Filtering, Pattern Matching, and Sorting
-- --------------------------------------------------------------------

-- Task 4A: Filter by exact category and sort price from highest to lowest
SELECT product_name, category, price 
FROM products 
WHERE category = 'Electronics'
ORDER BY price DESC;

-- Task 4B: The Ultimate Combo
-- Filters using LIKE, ensures items are in stock, and sorts alphabetically
SELECT product_name, category, price, stock_quantity
FROM products 
WHERE product_name LIKE '%Chair%' 
  AND stock_quantity > 0
ORDER BY product_name ASC;