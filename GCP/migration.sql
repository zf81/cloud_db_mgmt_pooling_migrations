CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 89e4c188ed68

ALTER TABLE patients DROP COLUMN allergies;

INSERT INTO alembic_version (version_num) VALUES ('89e4c188ed68');

-- Running upgrade 89e4c188ed68 -> 01629407d7ff

ALTER TABLE patients ADD COLUMN happiness_score INTEGER;

UPDATE alembic_version SET version_num='01629407d7ff' WHERE alembic_version.version_num = '89e4c188ed68';

