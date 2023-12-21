CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 38f83bd742c8

INSERT INTO alembic_version (version_num) VALUES ('38f83bd742c8');

-- Running upgrade 38f83bd742c8 -> d1de466cf311

ALTER TABLE patients ADD COLUMN sadness_score INTEGER;

ALTER TABLE patients ADD COLUMN favorite_tv_show VARCHAR(50) NOT NULL;

UPDATE alembic_version SET version_num='d1de466cf311' WHERE alembic_version.version_num = '38f83bd742c8';

