CREATE VIEW experiments_view AS
    SELECT
        experiments.experiment_id AS id,
        experiments.name AS name,
        organisms.name AS organism,
        probes.name AS probe
    FROM experiments
    JOIN organisms ON experiments.organism_id = organisms.id
    JOIN probes ON experiments.probe_id = probes.id