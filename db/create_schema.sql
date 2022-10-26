CREATE DATABASE app_database;

CREATE USER IF NOT EXISTS app_user WITH PASSWORD '123app';

ALTER ROLE app_user SET client_encoding TO 'utf8';
ALTER ROLE app_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE app_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE app_database TO app_user;

--
--CREATE SCHEMA IF NOT EXISTS content;
--
--CREATE TABLE IF NOT EXISTS content.data (
--    id uuid PRIMARY KEY,
--    title TEXT NOT NULL,
--    description TEXT,
--    image TEXT,
--    creation_date DATE,
--    created timestamp with time zone,
--    modified timestamp with time zone
--);

