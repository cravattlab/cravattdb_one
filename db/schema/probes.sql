CREATE TABLE IF NOT EXISTS probes (
    id SERIAL UNIQUE,
    name varchar(100),
    structure text
);

CREATE INDEX ON probes (name);