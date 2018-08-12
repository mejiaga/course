INSERT INTO favorite_foods (food, score)
VALUES ("Spaghetti", 8);

INSERT INTO favorite_foods (food, score)
VALUES ("Pizza", 10);

INSERT INTO favorite_foods (food, score)
VALUES ("Tuna Casserole", 2);

SELECT * FROM favorite_foods;

---

INSERT INTO favorite_songs (song, artist, score)
VALUES ("Papercut", "Zedd", 8);

INSERT INTO favorite_songs (song, artist, score)
VALUES ("Pinball Wizard", "The Who", 7);

INSERT INTO favorite_songs (song, artist, score)
VALUES ("Sad Machine", "Porter Robinson", 10);

SELECT * FROM favorite_songs;

---

INSERT INTO favorite_movies (movie, five_times, score)
VALUES ("Citizen Kane", true, 9),("Bladerunner", true, 10), ("Pup Star", false, 2);

SELECT * FROM favorite_movies;

