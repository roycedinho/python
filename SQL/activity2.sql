DROP TABLE IF EXISTS Salesman;
DROP TABLE IF EXISTS Orders;

CREATE TABLE Salesman (
    Salesman_ID TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    Commission REAL
);

INSERT INTO Salesman (Salesman_ID, name, city, Commission) VALUES 
('5001', 'AJ Tracey', 'Brussels', 0.21),
('5002', 'Austin', 'Cape Town', 0.33),
('5003', 'Travis', 'Zurich', 0.12),
('5004', 'Fein', 'Bristol', 0.24),
('5005', 'David', 'Le Chesnay', 0.23),
('5006', 'Hank', 'Charlotte', 0.41);

CREATE TABLE Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT,
    FOREIGN KEY (salesman_id) REFERENCES Salesman(Salesman_ID)
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES 
('70001', 150.5, '2024-06-01', '3005', '5001'),
('70002', 270.65, '2024-06-02', '3001', '5002'),
('70003', 65.26, '2024-06-03', '3002', '5003'),
('70004', 110.5, '2024-10-04', '3003', '5004'),
('70005', 948.5, '2024-10-05', '3004', '5005'),
('70006', 2400.6, '2024-10-06', '3005', '5006');


SELECT * FROM Salesman;
SELECT * FROM Orders;

SELECT name, Commission
FROM Salesman;