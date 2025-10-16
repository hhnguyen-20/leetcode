# Write your MySQL query statement below
DELETE b.*
FROM Person a
JOIN Person b ON a.email = b.email AND a.id < b.id;
