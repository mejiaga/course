CREATE DATABASE programming_db;

USE programming_db;

CREATE TABLE programming_languages(
  -- Creates a numeric column called "id" that will automatically increment its default value as we create new rows. --
  id INTEGER(11) AUTO_INCREMENT NOT NULL,
  language VARCHAR(20),
  popularity INTEGER(11),
  -- Creates a boolean column called "mastered" which will automatically fill --
  -- with TRUE when a new row is made, unless defined otherwise. --
  mastered BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (id)
);

-- Creates new rows 
INSERT INTO programming_languages (language, popularity)
VALUES ("JavaScript", 95);

INSERT INTO programming_languages (language, popularity)
VALUES ("Python", 84);

INSERT INTO programming_languages (language, popularity)
VALUES ("HTML", 100);

INSERT INTO programming_languages (language, popularity)
VALUES ("MySQL", 70);

SELECT * FROM programming_languages;
