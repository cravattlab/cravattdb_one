CREATE TABLE IF NOT EXISTS cell_lines (
    id SERIAL UNIQUE,
    name varchar(100),
    description text,
    synonyms text
);