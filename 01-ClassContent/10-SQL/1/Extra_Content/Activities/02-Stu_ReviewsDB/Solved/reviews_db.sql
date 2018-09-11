-- Creates the "favorite_db" database --
CREATE DATABASE favorites_db;

-- Makes it so all of the following code will affect favorite_db --
USE favorites_db;

-- Creates the table "favorite_foods" within favorite_db --
CREATE TABLE food_reviews (
  -- Makes a column of string values called "food" that cannot contain null values --
  food VARCHAR(50) NOT NULL,
  -- Makes an numeric column called "score" --
  score INTEGER(10)
);

CREATE TABLE song_reviews (
  song VARCHAR(100) NOT NULL,
  artist VARCHAR(50),
  score INTEGER(10)
);

CREATE TABLE film_reviews (
  -- Creates a numeric column called "id" that automatically increments and cannot be null --
  id INTEGER(11) AUTO_INCREMENT NOT NULL,
  movie VARCHAR(100) NOT NULL,
  -- Creates a boolean column called "released_on_bluray" that sets the default value to FALSE if nothing is entered --
  released_on_bluray BOOLEAN DEFAULT FALSE,
  score INTEGER(10),
  -- Sets the primary key of the table to id --
  PRIMARY KEY (id)
);
