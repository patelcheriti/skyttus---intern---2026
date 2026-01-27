--count total number of students.
SELECT COUNT(*) AS "Total Students"
FROM students;

--find average marks of students.
select avg(marks) as "average marks"
from students;

--find highest and lowest marks.
select min(marks) as "Lowest marks" , max(marks) as "Highest marks"
from students;

--find department-wise average marks.
select department , avg(marks) as "Avg marks"
from students
group by department;

--display departments where average marks > 70.
select department , avg(marks) as "Avg marks"
from students
group by department
having avg(marks) > 70;