-- 4-never_empty.sql
-- Creates a table named id_not_null with id and name columns
-- The id column has a default value of 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
