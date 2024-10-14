# Write your MySQL query statement below

select *
from cinema
where MOD(id,2)<>0 and lower(description) <> 'boring'
order by rating DESC;
