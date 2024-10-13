# Write your MySQL query statement below
SELECT DISTINCT a1.player_id, MIN(a1.event_date) AS first_login
FROM activity a1
GROUP BY a1.player_id


