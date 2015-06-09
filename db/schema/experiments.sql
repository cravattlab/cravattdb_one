CREATE TABLE IF NOT EXISTS experiments (
    experiment_id SERIAL UNIQUE,
    experiment_type integer references experiment_types(id),
    sample_type integer references sample_types(id),
    organism_id integer references organisms(id),
    probe_id integer references probes(id),
    name varchar(100),
    description text,
    annotations hstore
);

CREATE INDEX ON experiments (experiment_type);
CREATE INDEX ON experiments (sample_type);
CREATE INDEX ON experiments (organism_id);
CREATE INDEX ON experiments (probe_id);
CREATE INDEX ON experiments (name);