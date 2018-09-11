CREATE DATABASE favorites_db;

-- Make it so all of the following code will affect favorite_db --

-- Creates the table "food_reviews" within favorite_db --
CREATE TABLE food_reviews (
  -- Make a column of string values called "food" that cannot contain null --
  -- Make an numeric column called "score" --
);

CREATE TABLE song_reviews (
  -- Make a column of string values called "song" that cannot contain null values --
  -- Make a string column called "artist" --
  -- Make an integer column called "score" --
  score INTEGER(10)
);

CREATE TABLE film_reviews (
  -- Create a numeric column called "id" that automatically increments and cannot be null --
  -- Create a string column called "movie" which cannot be null --
  -- Create a boolean column called "released_on_bluray" that sets the default value to FALSE if nothing is entered --
  -- Make an integer column called "score" --
  -- Set the primary key of the table to id --
);
