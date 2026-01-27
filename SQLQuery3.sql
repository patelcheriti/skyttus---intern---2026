--assessment4-subqueries

--find employees earning more than average salary.
select emp_name , salary
from employees 
where salary > ( 
select avg(salary)
from employees);

--find department with highest total salary.
select e2.dept_name , sum(salary) as Total_salary
from employees e1 join departments e2
on e1.dept_id = e2.dept_id
group by e2.dept_name
order by Total_salary desc;

--display employee with second highest salary.
select emp_name, salary
from employees
where salary = (
    select MAX(salary)
    from employees
    where salary < (
        select MAX(salary)
        from employees));

--display employees working in same department as "Diya".
select emp_name
from employees
where dept_id = (select dept_id
from employees
where emp_name = 'Diya');