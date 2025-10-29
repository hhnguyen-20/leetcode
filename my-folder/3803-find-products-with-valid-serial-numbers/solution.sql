# Write your MySQL query statement below
SELECT *
FROM products
WHERE description REGEXP '(?-i)\\bSN[0-9]{4}-[0-9]{4}\\b'
ORDER BY 1;
