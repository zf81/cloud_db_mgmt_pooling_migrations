CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 8d59bd36bb5a

INSERT INTO alembic_version (version_num) VALUES ('8d59bd36bb5a');

