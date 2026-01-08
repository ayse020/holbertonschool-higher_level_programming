-- Lists all records of the table second_table by descending score, and with a non-empty name
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
