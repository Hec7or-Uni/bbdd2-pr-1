# PostgreSQL

## Como empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  postgres:
    image: postgres:15
    restart: always
    ports:
      - 5432:5432
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      PGDATA: /var/lib/postgresql/data/pgdata
    volumes:
      - ./data:/var/lib/postgresql/data

```

```bash
docker-compose up -d
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
  fechaNacimiento  TIMESTAMP       NOT NULL,
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
CREATE ROLE developer WITH
  LOGIN
  PASSWORD 'mypassword'
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION;

GRANT SELECT, INSERT, UPDATE ON books, users, rent TO developer;
```

```sql
CREATE ROLE client WITH
  LOGIN
  PASSWORD 'mypassword'
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION;

GRANT SELECT ON books, rent TO client;

```
