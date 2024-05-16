# Write your MySQL query statement below
SELECT user_id as id, COUNT(*) AS num
FROM (
    SELECT requester_id AS user_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id
    FROM RequestAccepted
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;

