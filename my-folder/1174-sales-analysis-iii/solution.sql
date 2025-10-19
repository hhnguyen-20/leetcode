# Write your MySQL query statement below
WITH SaleDates AS (
    SELECT 
        s.product_id, 
        MIN(s.sale_date) AS earliest_sale_date,
        MAX(s.sale_date) AS latest_sale_date   
    FROM Sales s
    GROUP BY s.product_id
)
SELECT DISTINCT p.product_id, p.product_name
FROM Product p
JOIN SaleDates sd ON p.product_id = sd.product_id
WHERE sd.earliest_sale_date >= '2019-01-01' 
AND sd.latest_sale_date <= '2019-03-31';
