CREATE VIEW experiments_view AS
    SELECT
        experiments.experiment_id AS id,
        experiments.name AS name,
        users.name AS user,
        organisms.name AS organism,
        cell_lines.name AS cell_line,
        probes.name AS probe,
        inhibitors.name AS inhibitor
    FROM experiments
    JOIN users ON experiments.user_id = users.id
    JOIN organisms ON experiments.organism_id = organisms.id
    JOIN cell_lines ON experiments.cell_line = cell_lines.id
    JOIN probes ON experiments.probe_id = probes.id
    JOIN inhibitors ON experiments.inhibitor_id = inhibitors.id