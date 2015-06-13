CREATE TABLE IF NOT EXISTS ip2_searchparams (
    id SERIAL UNIQUE,
    experiment_type integer references experiment_types(id),
    data jsonb
);