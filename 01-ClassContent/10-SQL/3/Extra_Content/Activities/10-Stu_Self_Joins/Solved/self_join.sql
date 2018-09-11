SELECT A.employee_id, A.first_name, A.last_name, CONCAT(B.first_name, ' ', B.last_name) AS 'Supervisor'
FROM emps A
JOIN emps B
ON (A.supervisor_id = B.employee_id);
