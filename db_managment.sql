/*

    Author: Gustavo Ortega

    PostgreSQL Version: 16.3

    Notes:
      - Replace all values inside "<>" with your own values, replacing the symbols <> as well.
      - Before executing the queries to insert data in tables, run migrations and migrate.
*/

-- Steps to create the user and database.

CREATE USER <user> WITH PASSWORD <'password'>;
CREATE DATABASE <"database"> WITH OWNER <user>;
ALTER ROLE <user> SET client_encoding TO 'utf8';
ALTER ROLE <user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <"database"> TO <user>;
