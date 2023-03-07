# Apache Cassandra

## Cómo empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  cassandra:
    container_name: cassandra
    image: cassandra:4.0
    restart: always
    ports:
      - 9042:9042
    environment:
      CASSANDRA_CLUSTER_NAME: "cassandra-cluster"
      CASSANDRA_USER: "cassandra"
      CASSANDRA_PASSWORD: "cassandra"
    volumes:
      - ./etc/cassandra:/etc/cassandra
      - ./data:/var/lib/cassandra

```

Si se tiene instalado el cliente de terminal de Cassandra, cqlsh, se puede automatizar
todo el desarrollo de la práctica, ejecutando el fichero populate.sh, situado en este
directorio.

### Creación de las tablas

```cql
CREATE KEYSPACE practice1 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
```
```cql
CREATE TABLE practice1.books (
   titulo           TEXT,
   codigoInterno    TEXT,
   ISBN             TEXT,
   fechaPublicacion TIMESTAMP,
   autor            TEXT,
   edicion          INT,
   PRIMARY KEY (codigoInterno)
);
```
```cql
CREATE TABLE practice1.users (
   nombre           TEXT,
   fechaNacimiento TIMESTAMP,
   DNI              TEXT,
   genero           TEXT,
   PRIMARY KEY (DNI)
);
```
```cql
CREATE TABLE practice1.rent_by_book (
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP,
   books            TEXT,
   users            TEXT,
   titulo           TEXT,
   autor            TEXT,
   PRIMARY KEY (books, users, fecha)
);
```
```cql
CREATE TABLE practice1.rent_by_user (
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP,
   books            TEXT,
   users            TEXT,
   nombre           TEXT,
   genero           TEXT,
   PRIMARY KEY (users, books, fecha)
);
```

### Permisos

```cql
CREATE ROLE developer WITH LOGIN = TRUE AND ACCESS TO ALL DATACENTERS;
```
```cql
GRANT SELECT ON practice1.books TO developer;
GRANT MODIFY ON practice1.books TO developer;
GRANT ALTER ON practice1.books TO developer;
GRANT DROP ON practice1.books TO developer;
```
```cql
GRANT SELECT ON practice1.users TO developer;
GRANT MODIFY ON practice1.users TO developer;
GRANT ALTER ON practice1.users TO developer;
GRANT DROP ON practice1.users TO developer;
```
```cql
GRANT SELECT ON practice1.rent_by_book TO developer;
GRANT MODIFY ON practice1.rent_by_book TO developer;
GRANT ALTER ON practice1.rent_by_book TO developer;
GRANT DROP ON practice1.rent_by_book TO developer;
```
```cql
GRANT SELECT ON practice1.rent_by_user TO developer;
GRANT MODIFY ON practice1.rent_by_user TO developer;
GRANT ALTER ON practice1.rent_by_user TO developer;
GRANT DROP ON practice1.rent_by_user TO developer;
```
```cql
CREATE USER developer1 WITH PASSWORD 'mypassword';

GRANT developer TO developer1;
```
```cql
CREATE ROLE client WITH LOGIN = TRUE AND ACCESS TO ALL DATACENTERS;
```
```cql
GRANT SELECT ON practice1.books TO client;

GRANT SELECT ON practice1.rent_by_book TO client;

GRANT SELECT ON practice1.rent_by_user TO client;

CREATE USER client1 WITH PASSWORD 'mypassword';
```
```cql
GRANT client TO client1;
```
