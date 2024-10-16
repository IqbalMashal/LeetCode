/* Write your PL/SQL query statement below */


SELECT r.contest_id AS contest_id, 
       ROUND(COUNT(r.user_id) * 100.0 / (SELECT COUNT(user_id) FROM users),2) AS percentage
FROM register r 
JOIN users u ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id;
