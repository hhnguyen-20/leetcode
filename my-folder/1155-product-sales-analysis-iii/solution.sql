# Write your MySQL query statement below
WITH FirstRelease AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) 
SELECT
    s.product_id,
    f.first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN FirstRelease f ON s.product_id = f.product_id
WHERE s.year = f.first_year;
