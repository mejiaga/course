CREATE TABLE emps(
 employee_id int(8) NOT NULL,
 first_name varchar(125) NOT NULL,
 last_name varchar(125) NOT NULL,
 supervisor_id int(8),
 PRIMARY KEY(employee_id)
);

INSERT INTO emps VALUES (25, 'Sandy', 'Waxman', 100);
INSERT INTO emps VALUES (26, 'Yukio', 'Mishima', 100);
INSERT INTO emps VALUES (27, 'Serge', 'Gainsbourg', 100);
INSERT INTO emps VALUES (100, 'Sidney', 'Meiru', 100);

