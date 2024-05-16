# Write your MySQL query statement below
delete b.*
from Person a
left join Person b on a.email = b.email
where a.id < b.id
