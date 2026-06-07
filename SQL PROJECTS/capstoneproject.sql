-- =============================================
-- SQL CAPSTONE PROJECT - 1
-- Covers: Table Creation, Data Manipulation, 
--         Filtering, Sorting & Analysis
-- =============================================

-- 1. Create Tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT CHECK (age >= 15 AND age <= 25),
    grade CHAR(1),
    enrollment_date DATE,
    gpa DECIMAL(3,2) CHECK (gpa >= 0 AND gpa <= 4.0),
    city VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INT,
    score DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- 2. Data Manipulation (INSERT)
INSERT INTO students (student_id, first_name, last_name, age, grade, enrollment_date, gpa, city) VALUES
(1, 'Alice', 'Johnson', 18, 'A', '2025-09-01', 3.85, 'Lagos'),
(2, 'Bob', 'Smith', 19, 'B', '2025-09-01', 3.20, 'Abuja'),
(3, 'Charlie', 'Brown', 17, 'A', '2025-09-15', 3.95, 'Lagos'),
(4, 'Diana', 'Prince', 18, 'C', '2025-08-20', 2.75, 'Port Harcourt'),
(5, 'Eve', 'Adams', 20, 'A', '2025-09-10', 3.65, 'Abuja'),
(6, 'Frank', 'White', 19, 'B', '2025-09-05', 3.10, 'Lagos');

INSERT INTO courses (course_id, course_name, student_id, score) VALUES
(101, 'Mathematics', 1, 92),
(102, 'Physics', 1, 88),
(103, 'Mathematics', 2, 75),
(104, 'Biology', 3, 95),
(105, 'Chemistry', 4, 65),
(106, 'Mathematics', 5, 89),
(107, 'Physics', 6, 78);

-- 3. Data Manipulation 
UPDATE students 
SET gpa = 3.45 
WHERE student_id = 2;

DELETE FROM students 
WHERE gpa < 2.5;   

-- 4. Analysis Queries (Filtering + Sorting)
-- Filter by grade and sort by GPA
SELECT 
    student_id,
    first_name,
    last_name,
    grade,
    gpa,
    city
FROM students 
WHERE grade = 'A' 
ORDER BY gpa DESC;

-- Students from Lagos with GPA above 3.5
SELECT * FROM students 
WHERE city = 'Lagos' AND gpa > 3.5 
ORDER BY age ASC;

--  Join tables + analysis
SELECT 
    s.first_name,
    s.last_name,
    c.course_name,
    c.score,
    s.gpa
FROM students s
JOIN courses c ON s.student_id = c.student_id
WHERE c.score >= 80
ORDER BY c.score DESC;

--  Summary statistics
SELECT 
    grade,
    COUNT(*) AS num_students,
    AVG(gpa) AS avg_gpa,
    MIN(age) AS youngest,
    MAX(gpa) AS highest_gpa
FROM students
GROUP BY grade
ORDER BY avg_gpa DESC;

SELECT 'Capstone Project Completed Successfully' AS status;