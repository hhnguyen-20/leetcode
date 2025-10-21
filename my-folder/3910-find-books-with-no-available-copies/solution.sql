# Write your MySQL query statement below
WITH borrowing AS (
    SELECT br.book_id, COUNT(*) AS current_borrowers
    FROM borrowing_records br
    WHERE br.return_date IS NULL
    GROUP BY br.book_id
)
SELECT 
    l.book_id, 
    l.title, 
    l.author, 
    l.genre, 
    l.publication_year, 
    b.current_borrowers
FROM library_books l
JOIN borrowing b ON l.book_id = b.book_id
WHERE b.current_borrowers >= 1 
AND (l.total_copies - b.current_borrowers) = 0
ORDER BY b.current_borrowers DESC, l.title;
