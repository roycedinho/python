-- ====================================================================
-- SQL SORTING, FILTERING & AGGREGATION assignment
-- ====================================================================

CREATE TABLE sales_records (
    order_id INT,
    product_name VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    store_region VARCHAR(50)
);

INSERT INTO sales_records (order_id, product_name, category, quantity, unit_price, store_region) VALUES
(1, 'Gaming Laptop', 'Electronics', 2, 1200.00, 'North'),
(2, 'Wireless Mouse', 'Electronics', 15, 25.00, 'North'),
(3, 'Office Chair', 'Furniture', 5, 150.00, 'South'),
(4, 'Desk Lamp', 'Furniture', 8, 45.00, 'East'),
(5, '4K Monitor', 'Electronics', 4, 350.00, 'West'),
(6, 'Drawing Pad', 'Electronics', 1, 90.00, 'South'),
(7, 'Filing Cabinet', 'Furniture', 3, 200.00, 'North'),
(8, 'Ballpoint Pens', 'Stationery', 100, 1.50, 'East');

SELECT 
    category,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_items_sold,
    SUM(quantity * unit_price) AS total_revenue,
    AVG(unit_price) AS average_item_price
FROM sales_records


WHERE store_region != 'East'


GROUP BY category

)
HAVING SUM(quantity * unit_price) > 500


ORDER BY total_revenue DESC;

