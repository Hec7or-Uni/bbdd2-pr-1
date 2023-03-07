# IBM DB2

## Como empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  db2:
    image: ibmcom/db2
    container_name: contenedor_db2
    restart: always
    privileged: true
    ports:
      - 50000:50000
    environment:
      LICENSE: accept
      DB2INST1_PASSWORD: db2inst1
      DBNAME: db2inst1
      PERSISTENT_HOME: "false" # (default: true) Specify to false if you are running Docker for Windows.
      ARCHIVE_LOGS: "false" # (default: true) Specify false to not configure log archiving (reduces start up time)
      TEXT_SEARCH: "false" # (default: false) Specify true to enable and configure text search
    volumes:
      - ./data:/database

```

```bash
docker-compose up -d
docker exec -it contenedor_db2 bash
su - db2inst1
db2start
db2 create database bbdd2
db2 connect to bbdd2 user db2inst1 using db2inst1
```

### Creación de las tablas
En db2 a la hora de crear las tablas aunque un parametro sea
clave primaria hay que indicar que es not null para que no 
de errores. Esto se pone siempre porque las claves primarias
no pueden ser nulas.

```sql
CREATE TABLE books (
   titulo           VARCHAR(255)    NOT NULL,
   codigoInterno    VARCHAR(36)     NOT NULL PRIMARY KEY,
   ISBN             VARCHAR(13)     NOT NULL,
   fechaPublicacion TIMESTAMP       NOT NULL,
   autor            VARCHAR(255)    NOT NULL,
   edicion          INT             NOT NULL
);
```

```sql
CREATE TABLE users (
   nombre           VARCHAR(255)    NOT NULL,
   fechaNacimiento  TIMESTAMP       NOT NULL,
   DNI              VARCHAR(9)      NOT NULL PRIMARY KEY,
   genero           VARCHAR(6)      NOT NULL
);
```

```sql
CREATE TABLE rent (
   books            VARCHAR(36)		NOT NULL,
   users            VARCHAR(9)		NOT NULL,
   fecha            TIMESTAMP 		NOT NULL,
   fechaDevolucion  TIMESTAMP       NOT NULL,
   PRIMARY KEY (books, users, fecha),
   FOREIGN KEY (books) REFERENCES books(codigoInterno),
   FOREIGN KEY (users) REFERENCES users(DNI)
);
```

### Permisos

```sql
CREATE ROLE developer;
GRANT CONNECT ON DATABASE TO developer;
GRANT SELECT, INSERT, UPDATE ON books TO developer;
GRANT SELECT, INSERT, UPDATE ON users TO developer;
GRANT SELECT, INSERT, UPDATE ON rent TO developer;
```

```sql
CREATE ROLE client;
GRANT CONNECT ON DATABASE TO client;
GRANT SELECT ON books TO client;
GRANT SELECT ON users TO client;
GRANT SELECT ON rent TO client;
```

```sql
GRANT DBADM ON DATABASE TO USER adminUsr -- Crear usuario admin con permisos de administrador
```
```sql
GRANT CONNECT ON DATABASE TO USER developerUsr;
```
```sql
GRANT CONNECT ON DATABASE TO USER clientUsr;
```
```sql
GRANT developer TO developerUsr;
GRANT client TO clientUsr
```
