# IBM DB2

## Como empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  db2:
    image: ibmcom/db2
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
```

```bash
su - db2inst1
```

```bash
db2start
```

### Creación de las tablas

```sql
CREATE TABLE books (
   titulo           VARCHAR(255)    NOT NULL,
   codigoInterno    VARCHAR(36)     PRIMARY KEY,
   ISBN             VARCHAR(13)     NOT NULL,
   fechaPublicacion TIMESTAMP       NOT NULL,
   autor            VARCHAR(255)    NOT NULL,
   edicion          INT             NOT NULL
);
```

```sql
CREATE TABLE users (
   nombre           VARCHAR(255)    NOT NULL,
   fechaNacimiento TIMESTAMP       NOT NULL,
   DNI              VARCHAR(9)      PRIMARY KEY,
   genero           VARCHAR(6)      NOT NULL
);
```

```sql
CREATE TABLE rent (
   books            VARCHAR(36),
   users            VARCHAR(9),
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP       NOT NULL,
   PRIMARY KEY (books, users, fecha),
   FOREIGN KEY (books) REFERENCES books(codigoInterno),
   FOREIGN KEY (users) REFERENCES users(DNI)
);
```

### Permisos

```sql
CREATE USER developer WITH PASSWORD 'PASSWORD';
GRANT CONNECT ON DATABASE TO developer;
GRANT SELECT, INSERT, UPDATE ON books, users, rent TO developer;
```

```sql
CREATE USER client WITH PASSWORD 'PASSWORD';
GRANT CONNECT ON DATABASE TO client;
GRANT SELECT ON books, users, rent TO client;
```
