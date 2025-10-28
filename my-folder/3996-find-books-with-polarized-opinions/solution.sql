# Write your MySQL query statement below
WITH polarized_books AS (
    SELECT 
        b.*, 
        MAX(r.session_rating) - MIN(r.session_rating) AS rating_spread,
        ROUND((
            SELECT SUM(IF(r4.session_rating >= 4 OR r4.session_rating <= 2, 1, 0))
            FROM reading_sessions r4
            WHERE r4.book_id = b.book_id
        ) / (
            SELECT COUNT(*)
            FROM reading_sessions r5
            WHERE r5.book_id = b.book_id
        ), 2) AS polarization_score
    FROM books b
    JOIN reading_sessions r ON b.book_id = r.book_id
    WHERE EXISTS (
        SELECT 1 
        FROM reading_sessions r2 
        WHERE b.book_id = r2.book_id
        HAVING MAX(r2.session_rating) >= 4 AND MIN(r2.session_rating) <= 2
    )
    GROUP BY b.book_id HAVING COUNT(r.session_id) >= 5 
)
SELECT DISTINCT p.*
FROM polarized_books p
JOIN reading_sessions r3 ON p.book_id = r3.book_id
ORDER BY polarization_score DESC, title DESC;
