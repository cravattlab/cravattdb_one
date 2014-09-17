CREATE TABLE IF NOT EXISTS organisms (
    id SERIAL UNIQUE,
    name varchar(100),
    tax_id int
);