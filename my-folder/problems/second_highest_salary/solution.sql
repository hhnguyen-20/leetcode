# Write your MySQL query statement below
select coalesce(max(salary), null) as SecondHighestSalary
from Employee
where salary < (
    select coalesce(max(salary), null)
    from Employee
);