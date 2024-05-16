# Write your MySQL query statement below
select visited_on,
       (
           select sum(amount)
           from Customer
           where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
       ) as amount,
       (
           select round(sum(amount) / 7,2)
           from Customer
           where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
       ) as average_amount
from Customer c
where visited_on >= (
    select date_add(min(visited_on), interval 6 day)
    from Customer
)
group by 1
order by visited_on;

