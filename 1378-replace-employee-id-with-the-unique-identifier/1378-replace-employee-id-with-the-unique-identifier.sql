# Write your MySQL query statement below
select uni.unique_id, em.name
from Employees em left join employeeUNI uni
on em.id = uni.id
