CREATE TABLE sales_data (
    product_id INT,
    product_name VARCHAR(50),
    category VARCHAR(50),
    quantity_sold INT,
    price_per_unit DECIMAL(10,2),
    total_revenue DECIMAL(10,2)
);

INSERT INTO sales_data (product_id, product_name, category, quantity_sold, price_per_unit, total_revenue) VALUES
(101, 'Laptop', 'Electronics', 5, 1000.00, 5000.00),
(102, 'Mouse', 'Electronics', 20, 25.00, 500.00),
(103, 'Desk Chair', 'Furniture', 4, 150.00, 600.00),
(104, 'Notebook', 'Stationery', 50, 2.00, 100.00),
(105, 'Monitor', 'Electronics', 10, 200.00, 2000.00),
(106, 'Office Desk', 'Furniture', 2, 300.00, 600.00);


SELECT 
    COUNT(product_id) AS total_unique_products,
    SUM(quantity_sold) AS total_items_sold,
    AVG(price_per_unit) AS average_product_price,
    MIN(total_revenue) AS lowest_single_sale,
    MAX(total_revenue) AS highest_single_sale
FROM sales_data;


SELECT 
    category,
    COUNT(product_id) AS number_of_items,
    SUM(quantity_sold) AS total_quantity_by_category,
    SUM(total_revenue) AS total_revenue_by_category
FROM sales_data
GROUP BY category;

SELECT 
    category,
    SUM(total_revenue) AS high_performing_revenue
FROM sales_data
GROUP BY category
HAVING SUM(total_revenue) > 1000
ORDER BY high_performing_revenue DESC;


-- CLEANUP (Optional)
-- Removes the table when done testing
DROP TABLE sales_data;