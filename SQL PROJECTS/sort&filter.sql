-- =============================================
-- SORT & FILTER ACTIVITY
-- Focus: Aggregate Functions, GROUP BY, 
--        HAVING, WHERE, ORDER BY
-- =============================================

-- 1. Create Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    sale_date DATE,
    region VARCHAR(50)
);

-- 2. Insert Sample Data
INSERT INTO sales (sale_id, product_name, category, quantity, unit_price, sale_date, region) VALUES
(1, 'Laptop', 'Electronics', 5, 1200.00, '2026-05-01', 'South'),
(2, 'Mouse', 'Electronics', 25, 25.00, '2026-05-05', 'North'),
(3, 'Notebook', 'Stationery', 100, 8.50, '2026-05-10', 'South'),
(4, 'Laptop', 'Electronics', 3, 1150.00, '2026-05-15', 'South'),
(5, 'Pen Pack', 'Stationery', 200, 4.99, '2026-05-20', 'North'),
(6, 'Headphones', 'Electronics', 12, 85.00, '2026-05-22', 'South'),
(7, 'Book', 'Education', 45, 22.00, '2026-05-25', 'North'),
(8, 'Keyboard', 'Electronics', 8, 65.00, '2026-05-28', 'South');

-- 3. Core Sort & Filter Queries

-- Query 1: Basic Filter + Sort
SELECT * FROM sales 
WHERE category = 'Electronics' 
ORDER BY unit_price DESC;

-- Query 2: Filter by region and quantity
SELECT 
    product_name,
    quantity,
    unit_price,
    (quantity * unit_price) AS total_value
FROM sales 
WHERE region = 'South' AND quantity >= 5
ORDER BY total_value DESC;

-- Query 3: Aggregate Functions with GROUP BY
SELECT 
    category,
    COUNT(*) AS num_transactions,
    SUM(quantity) AS total_items_sold,
    AVG(unit_price) AS avg_price,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Query 4: GROUP BY + HAVING (filter groups)
SELECT 
    region,
    category,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY region, category
HAVING SUM(quantity * unit_price) > 1000
ORDER BY revenue DESC;

-- Query 5: Advanced - Top performing products
SELECT 
    product_name,
    category,
    SUM(quantity) AS total_sold,
    SUM(quantity * unit_price) AS revenue
FROM sales
WHERE sale_date BETWEEN '2026-05-01' AND '2026-05-31'
GROUP BY product_name, category
HAVING SUM(quantity) >= 10
ORDER BY revenue DESC
LIMIT 5;

-- End of Sort & Filter Script
SELECT 'Sort & Filter Activity Completed Successfully' AS status;