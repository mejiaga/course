INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Jacob", true, "Misty", 10);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Ahmed", true, "Rockington", 100);

INSERT INTO people (name)
VALUES ("Peter");

UPDATE people
SET has_pet = true
WHERE name = "Peter";

SELECT * FROM people;
