# Write your MySQL query statement below

-- SELECT name AS Customers
-- FROM customers
-- EXCEPT
-- SELECT c.name
-- FROM customers c
-- JOIN orders o
-- ON c.id = o.customerid;

SELECT name AS Customers
FROM customers
WHERE id NOT IN (
    SELECT o.customerid
    FROM orders o
);