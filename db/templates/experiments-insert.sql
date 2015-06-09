INSERT INTO experiments (
    experiment_type,
    sample_type,
    organism_id,
    probe_id,
    name,
    description
) VALUES (
    %(experiment_type)s,
    %(sample_type)s,
    %(organism)s,
    %(probe)s,
    %(name)s,
    %(description)s
) RETURNING experiment_id;