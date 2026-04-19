CREATE TABLE IF NOT EXISTS PRODUCT(
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE TEXT,
    PRO_COM TEXT
);

-- Insert into PRODUCT(PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM)
INSERT INTO PRODUCT (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
(101, 'Gaming Laptop', '1200', '15'),
(102, 'Wireless Keyboard', '450', '16'),
(103, 'USB Flash Drive', '250', '14'),
(104, 'Bluetooth Speaker', '550', '16'),
(105, 'Curved Monitor', '5000', '11'),
(106, 'External DVD Drive', '900', '12'),
(107, 'Blu-ray Drive', '800', '12'),
(108, 'Laser Printer', '2600', '13'),
(109, 'Ink Refill Kit', '350', '13'),
(110, 'Ergonomic Mouse', '250', '12');

SELECT pro_name, pro_price
FROM product
WHERE CAST(pro_price AS INTEGER) = (SELECT MAX(CAST(pro_price AS INTEGER)) FROM product);