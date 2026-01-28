--assessment9-sql coding test

--write query to find nth highest salary
select max(salary) as nth_highest_salary
from employees
where salary < (
		select max(salary)
		from employees);

--remove duplicate records
delete from employees
where emp_id not in (
        select min(emp_id)
        from employees
        group by emp_name, dept_id, salary);

--find records commom in two tables
                --create employee_backup table
                select * 
                into employee_backup 
                from employees;

                --insert records in employee_backup table
                insert into employee_backup values
                (108, 'Disha', 3, 58000),
                (109, 'Trusha', 1, 62000);
                
                --select * from employee_backup;

select e.*
from employees e inner join employee_backup b
on e.emp_id = b.emp_id;

--find employees hired in last 6 months
                --add hire_date column
                alter table employees
                add hire_date date;
                        --select * from employees;
                --update hire_date column
                update employees
                set hire_date = '2025-11-15'
                where emp_id = 101;
                update employees
                set hire_date = '2025-10-01'
                where emp_id = 102;
                update employees
                set hire_date = '2025-06-10'
                where emp_id = 103;
                update employees
                set hire_date = '2025-09-20'
                where emp_id = 104;
                update employees
                set hire_date = '2025-12-01'
                where emp_id = 105;
                update employees
                set hire_date = '2025-12-10'
                where emp_id = 106;
                update employees
                set hire_date = '2025-01-05'
                where emp_id = 107;
select * 
from employees 
where hire_date between '2025-07-28' and '2026-01-28';

--find continuous duplicate values
                --create log table
                create table logs(
                id int,
                value int);
                --insert values
                insert into logs values
                (1, 100),
                (2, 200),
                (3, 300),
                (4, 200),
                (5, 100),
                (6, 200),
                (7, 300),
                (8, 200);  --select * from logs;

select distinct value
from logs;

