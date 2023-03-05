CREATE ROLE developer WITH LOGIN = TRUE AND ACCESS TO ALL DATACENTERS;

GRANT SELECT ON practice1.books TO developer;
GRANT MODIFY ON practice1.books TO developer;
GRANT ALTER ON practice1.books TO developer;
GRANT DROP ON practice1.books TO developer;

GRANT SELECT ON practice1.users TO developer;
GRANT MODIFY ON practice1.users TO developer;
GRANT ALTER ON practice1.users TO developer;
GRANT DROP ON practice1.users TO developer;

GRANT SELECT ON practice1.rent_by_book TO developer;
GRANT MODIFY ON practice1.rent_by_book TO developer;
GRANT ALTER ON practice1.rent_by_book TO developer;
GRANT DROP ON practice1.rent_by_book TO developer;

GRANT SELECT ON practice1.rent_by_user TO developer;
GRANT MODIFY ON practice1.rent_by_user TO developer;
GRANT ALTER ON practice1.rent_by_user TO developer;
GRANT DROP ON practice1.rent_by_user TO developer;

CREATE USER developer1 WITH PASSWORD 'mypassword';

GRANT developer TO developer1;

CREATE ROLE client WITH LOGIN = TRUE AND ACCESS TO ALL DATACENTERS;

GRANT SELECT ON practice1.books TO client;

GRANT SELECT ON practice1.rent_by_book TO client;

GRANT SELECT ON practice1.rent_by_user TO client;

CREATE USER client1 WITH PASSWORD 'mypassword';

GRANT client TO client1;