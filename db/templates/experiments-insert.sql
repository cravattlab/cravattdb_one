INSERT INTO experiments (
    user_id,
    experiment_type,
    sample_type,
    organism_id,
    cell_line,
    probe_id,
    inhibitor_id,
    name,
    description
) VALUES (
    %(username)s,
    %(experiment_type)s,
    %(sample_type)s,
    %(organism)s,
    %(cell_line)s,
    %(probe)s,
    %(inhibitor)s,
    %(name)s,
    %(description)s
) RETURNING experiment_id;