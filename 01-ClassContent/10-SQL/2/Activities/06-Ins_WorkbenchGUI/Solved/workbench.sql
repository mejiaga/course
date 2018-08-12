-- Alter imported table to add an id
ALTER TABLE comcastfcccomplaints
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

-- Select all from the table
SELECT * FROM comcastfcccomplaints;