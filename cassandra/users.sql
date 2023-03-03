CREATE ROLE developer WITH LOGIN = TRUE AND ACCESS TO ALL DATACENTERS;

GRANT SELECT, MODIFY, ALTER, DROP, UPDATE ON KEYSPACE. books, users, rent_by_book, rent_by_user TO developer;

CREATE USER developer WITH PASSWORD = 'mypassword';

GRANT developer TO developer;

CREATE ROLE client WITH
  PASSWORD = 'mypassword' AND
  LOGIN = TRUE AND
  ACCESS TO ALL DATACENTERS
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION;

GRANT SELECT ON books, rent, rent_by_user, rent_by_book TO client;
