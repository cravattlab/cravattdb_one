CREATE TABLE IF NOT EXISTS experiment_types (
    id SERIAL UNIQUE,
    name varchar(100),
    description text
);