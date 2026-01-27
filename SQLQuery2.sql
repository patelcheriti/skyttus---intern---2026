create table employees (
emp_id int,
emp_name varchar(50),
dept_id int,
salary int
);

INSERT INTO employees (emp_id, emp_name, dept_id, salary) VALUES
(101, 'Cheriti', 2, 60000),
(102, 'Riya', 1, 45000),
(103, 'Diya', 2, 75000),
(104, 'Rutu', 3, 52000),
(105, 'Vrutti', 2, 48000),
(106, 'Tvisha', 4, 55000),
(107, 'Aarchi', NULL, 40000);

select * from employees;

create table departments (
dept_id int,
dept_name varchar(50),
);

INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Marketing');

select * from departments;

--display employee name with department name.
select e1.emp_name , e2.dept_name
from employees e1 join departments e2
on e1.dept_id = e2.dept_id;

--display employees earning more than 50,000.
select emp_name , salary
from employees
where salary > 50000;

--display department wise total salary.
select e2.dept_name , sum(salary) as "Total salary" 
from employees e1 join departments e2
on e1.dept_id = e2.dept_id
group by e2.dept_name;

--display departments with more than two employees.
select e2.dept_name , count(e1.emp_name) as "Employee count"
from employees e1 join departments e2
on e1.dept_id = e2.dept_id
group by e2.dept_name 
having count(e1.emp_name) > 2;

--display employees without a department.
select e1.emp_name 
from employees e1 left join departments e2
on e1.dept_id = e2.dept_id
where e2.dept_id is null;