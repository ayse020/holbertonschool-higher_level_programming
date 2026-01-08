-- Lists all cities of California using IN clause
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id;
