-- Create the STUDENT table if it does not exist
-- NOT NULL is used for NAME to ensure every student record has a
-- NAME
CREATE TABLE IF NOT EXISTS STUDENT (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

-- Insert sample data into the STUDENT table
INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
('1', 'Terry', 'Lagos', '********', 18),
('2', 'James', 'Jangalova', '********', 18),
('3', 'Simon', 'Miami', '********', 20),
('4', 'Zay', 'Lagos', '********', 18),
('5', 'Mofe', 'Florida', '********', 20),
('6', 'David', 'Atlanta', '********', 18);

-- Select all records from the STUDENT table to verify insertion
SELECT * FROM STUDENT;

-- Query students who are 18 years old and live in Lagos
SELECT * FROM STUDENT WHERE AGE = 18 AND ADDRESS = 'Lagos';

-- Query students who are 18 years old and named Terry
SELECT * FROM STUDENT WHERE AGE = 18 AND NAME = 'Terry';

-- Query students named Terry or Simon
SELECT * FROM STUDENT WHERE NAME = 'Terry' OR NAME = 'Simon';

-- Query students named Terry or aged 20
SELECT * FROM STUDENT WHERE NAME = 'Terry' OR AGE = 20;

-- Query students aged 18 and named Terry or James
SELECT * FROM STUDENT WHERE AGE = 18 AND (NAME = 'Terry' OR NAME = 'James');