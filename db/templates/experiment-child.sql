CREATE TABLE IF NOT EXISTS $table (
    PRIMARY KEY(id)
) INHERITS (experiment);

CREATE INDEX ON $table (peptide_index);
CREATE INDEX ON $table (ipi);
CREATE INDEX ON $table (symbol);