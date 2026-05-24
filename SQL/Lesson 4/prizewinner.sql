-- Create the NOBEL_WIN table if it does not exist
CREATE TABLE IF NOT EXISTS NOBEL_WIN (
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
);

-- INSERT SAMPLE DATA INTO THE NOBEL_WIN TABLE
INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES
(2020, 'Physics', 'Roger Penrose', 'United Kingdom', 'Nobel Prize in Physics'),
(2023, 'Chemistry', 'Emmanuelle Charpentier', 'France', 'Nobel Prize in Chemistry'),
(2024, 'Literature', 'Louise Glück', 'United States', 'Nobel Prize in Literature'),
(2018, 'Peace', 'World Food Programme', 'International', 'Nobel Peace Prize'),
(2022, 'Economics', 'Paul R. Milgrom and Robert B. Wilson', 'United States', 'Nobel Memorial Prize in Economic Sciences'),
(2021, 'Medicine', 'David Julius and Ardem Patapoutian', 'United States', 'Nobel Prize in Physiology or Medicine'),
(1972, 'Peace', 'Henry Kissinger and Le Duc Tho', 'United States and Vietnam', 'Nobel Peace Prize'),
(2019, 'Literature', 'Peter Handke', 'Austria', 'Nobel Prize in Literature'),
(2020, 'Chemistry', 'Jennifer Doudna and Emmanuelle Charpentier', 'United States and France', 'Nobel Prize in Chemistry'),
(2021, 'Physics', 'Syukuro Manabe and Klaus Hasselmann', 'United States and Germany', 'Nobel Prize in Physics'),
(2023, 'Medicine', 'Katalin Karikó and Drew Weissman', 'Hungary and United States', 'Nobel Prize in Physiology or Medicine');

-- Select all records where the subject does not start with 'P'
SELECT * FROM NOBEL_WIN
WHERE SUBJECT NOT LIKE 'P%';