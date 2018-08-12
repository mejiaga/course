-- Alter imported table to add an id
ALTER TABLE wordassociation
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

-- Select all with the source of AC
SELECT * FROM wordassociation
WHERE source = "AC";

-- Select all with the source of BC
SELECT * FROM wordassociation
WHERE source = "BC";

-- Select all with the source of CC
SELECT * FROM wordassociation
WHERE source = "CC";

-- Select all where the author is greater than 0 and less than 20
SELECT * FROM wordassociation
WHERE author >= 0 AND author <= 20;

-- Select all where either word is pie
SELECT * FROM wordassociation
WHERE word1 = "pie" OR word2 = "pie";

-- Find the lowest id whose source is CC
SELECT MIN(id) FROM wordassociation
WHERE source = "CC";

-- Find how many rows have an author of 12
SELECT COUNT(author)  FROM wordassociation
WHERE author = 12;
