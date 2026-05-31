-- DROP TABLES FIRST TO AVOID DUPLICATE ERRORS
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Salesman;

--------------------------------------------------
-- CREATE TABLES
--------------------------------------------------

CREATE TABLE Salesman (
    salesman_id INT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
);

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    grade INT,
    salesman_id INT,
    FOREIGN KEY (salesman_id) REFERENCES Salesman(salesman_id)
);

CREATE TABLE Orders (
    order_number TEXT PRIMARY KEY,
    purchase_amount DECIMAL(10,2),
    date DATE,
    customer_id INT,
    salesman_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (salesman_id) REFERENCES Salesman(salesman_id)
);

--------------------------------------------------
-- INSERT DATA
--------------------------------------------------

INSERT INTO Salesman VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5003, 'Pit Alex', 'London', 0.11),
(5004, 'Mc Lyon', 'Paris', 0.14),
(5005, 'Paul Adam', 'Rome', 0.12);

INSERT INTO Customer VALUES
(3002, 'Amy Elsner', 'Los Angeles', 200, 5002),
(3001, 'Ollie Brian', 'San Jose', 100, 5001),
(3004, 'Michael Adams', 'New York', 200, 5003),
(3003, 'Maria Anders', 'Berlin', 300, 5004),
(3005, 'Karl Jablonski', 'Chicago', 100, 5005);

INSERT INTO Orders VALUES
('70001', 150.50, '2024-01-10', 3002, 5002),
('70002', 270.65, '2024-01-15', 3001, 5001),
('70003', 65.26, '2024-01-20', 3004, 5003),
('70004', 110.50, '2024-01-25', 3003, 5004),
('70005', 948.50, '2024-01-30', 3005, 5005);

--------------------------------------------------
-- QUERIES
--------------------------------------------------

-- 1. Customers and salesmen from same city
SELECT c.customer_name,
       s.name AS salesman_name,
       c.city
FROM Customer c
JOIN Salesman s
ON c.city = s.city;

-- 2. Link customer to salesman
SELECT c.customer_name,
       s.name AS salesman_name
FROM Customer c
JOIN Salesman s
ON c.salesman_id = s.salesman_id;

-- 3. Orders where customer city != salesman city
SELECT o.order_number,
       c.customer_name,
       s.name AS salesman_name,
       c.city AS customer_city,
       s.city AS salesman_city
FROM Orders o
JOIN Customer c ON o.customer_id = c.customer_id
JOIN Salesman s ON o.salesman_id = s.salesman_id
WHERE c.city <> s.city;

-- 4. All orders with customer names
SELECT o.order_number,
       c.customer_name
FROM Orders o
JOIN Customer c ON o.customer_id = c.customer_id;

-- 5. Customers with grades
SELECT c.customer_name AS Customer,
       c.grade AS Grade
FROM Customer c
WHERE c.grade IS NOT NULL;

-- 6. Customers with salesmen commission between 0.12 and 0.14
SELECT c.customer_name,
       c.city,
       s.name AS salesman_name,
       s.commission
FROM Customer c
JOIN Salesman s ON c.salesman_id = s.salesman_id
WHERE s.commission BETWEEN 0.12 AND 0.14;

-- 7. Commission calculation for grade >= 200
SELECT o.order_number,
       c.customer_name,
       s.name AS salesman_name,
       s.commission AS "Commission %",
       o.purchase_amount * s.commission AS Commission
FROM Orders o
JOIN Customer c ON o.customer_id = c.customer_id
JOIN Salesman s ON o.salesman_id = s.salesman_id
WHERE c.grade >= 200;

-- 8. Orders on specific date
SELECT c.customer_name,
       o.order_number,
       o.date
FROM Customer c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.date = '2024-01-15';