CREATE TABLE IF NOT EXISTS experiments (
    experiment_id SERIAL UNIQUE,
    user_id integer references users(id),
    experiment_type integer references experiment_types(id),
    sample_type integer references sample_types(id),
    organism_id integer references organisms(id),
    cell_line integer references cell_lines(id),
    probe_id integer references probes(id),
    inhibitor_id integer references inhibitors(id),
    name varchar(100),
    description text,
    annotations hstore
);

CREATE INDEX ON experiments (user_id);
CREATE INDEX ON experiments (experiment_type);
CREATE INDEX ON experiments (sample_type);
CREATE INDEX ON experiments (organism_id);
CREATE INDEX ON experiments (cell_line);
CREATE INDEX ON experiments (probe_id);
CREATE INDEX ON experiments (inhibitor_id);
CREATE INDEX ON experiments (name);