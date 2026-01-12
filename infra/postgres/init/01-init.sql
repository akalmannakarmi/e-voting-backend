-- =========================
-- AUTH SERVICE
-- =========================

CREATE DATABASE auth_db;
CREATE USER auth_user WITH PASSWORD 'auth_password';

GRANT ALL PRIVILEGES ON DATABASE auth_db TO auth_user;

\connect auth_db

-- Auth user owns the public schema
ALTER SCHEMA public OWNER TO auth_user;

-- Ensure future tables/sequences are accessible
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO auth_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO auth_user;


-- =========================
-- BALLOT SERVICE
-- =========================

\connect postgres

CREATE DATABASE ballot_db;
CREATE USER ballot_user WITH PASSWORD 'ballot_password';

GRANT ALL PRIVILEGES ON DATABASE ballot_db TO ballot_user;

\connect ballot_db

ALTER SCHEMA public OWNER TO ballot_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO ballot_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO ballot_user;


-- =========================
-- VOTE SERVICE
-- =========================

\connect postgres

CREATE DATABASE vote_db;
CREATE USER vote_user WITH PASSWORD 'vote_password';

GRANT ALL PRIVILEGES ON DATABASE vote_db TO vote_user;

\connect vote_db

ALTER SCHEMA public OWNER TO vote_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO vote_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON SEQUENCES TO vote_user;

