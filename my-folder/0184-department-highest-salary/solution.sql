# Write your MySQL query statement below
WITH HighestSalary AS (
    SELECT
        e.departmentId AS DepartmentID,
        d.name AS Department,
        MAX(e.salary) AS HighestSalary
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
    GROUP BY e.departmentId
) 
SELECT 
    h.Department, 
    e2.name AS Employee, 
    e2.salary AS Salary
FROM Employee e2
JOIN HighestSalary h ON e2.departmentId = h.DepartmentID
WHERE e2.salary = h.HighestSalary
ORDER BY h.Department, e2.name;
