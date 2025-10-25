# Write your MySQL query statement below
WITH Dates AS (
    SELECT 
        student_id, 
        subject, 
        MIN(exam_date) AS earliest, 
        MAX(exam_date) AS latest
    FROM Scores
    GROUP BY student_id, subject
)
SELECT 
    s1.student_id,
    s1.subject,
    s1.score AS first_score,
    s2.score AS latest_score
FROM Scores s1
JOIN Scores s2 ON s1.student_id = s2.student_id 
    AND s1.subject = s2.subject 
JOIN Dates d ON s2.student_id = d.student_id 
    AND s2.subject = d.subject
WHERE s1.score < s2.score AND s1.exam_date = earliest AND s2.exam_date = latest
GROUP BY s1.student_id, s1.subject
ORDER BY s1.student_id, s1.subject;
