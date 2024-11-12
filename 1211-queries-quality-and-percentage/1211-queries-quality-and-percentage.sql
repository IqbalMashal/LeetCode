SELECT 
    query_name, 
    ROUND(AVG(rating / position), 2) AS quality, 
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage 
FROM 
    queries 
GROUP BY 
    query_name
HAVING 
    query_name IS NOT NULL;