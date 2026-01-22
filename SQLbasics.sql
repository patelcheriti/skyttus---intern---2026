CREATE TABLE students(
	student_id INT PRIMARY KEY,
	name VARCHAR(50),
	department VARCHAR(30),
	year INT,
	marks INT
);

insert into students values 
(1, 'Cheriti', 'CSE', 3, 89),
(2, 'Riya', 'IT', 4, 95),
(3, 'Diya', 'MCA', 2, 79),
(4, 'Vrutti', 'CE', 4, 90),
(5, 'Rutu', 'BCA', 3, 80);

--display all the records.
SELECT * FROM STUDENTS;

--display only name and department.
SELECT name, department 
FROM students;

--find students with marks greater than 75.
SELECT * 
from students
where marks >75;

--display students from CSE department
select *
from students
where department = 'CSE';

--sort students by marks(desc).
select *
from students
order by marks desc;

--display top three scorers.
SELECT top 3 *
FROM students
ORDER BY marks DESC;
