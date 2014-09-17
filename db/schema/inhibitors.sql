CREATE TABLE IF NOT EXISTS inhibitors (
    id SERIAL UNIQUE,
    name varchar(100),
    structure text
);

CREATE INDEX ON inhibitors (name);