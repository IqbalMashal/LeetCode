SELECT user_id,
       UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM users
ORDER BY user_id;
