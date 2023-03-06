# Oracle-XE

## Como empezar

### Puesta en marcha

```yml
version: '3.9'

services:
  oracle:
    image: gvenzl/oracle-xe:21.3.0
    restart: always
    ports:
      - 1521:1521
    environment:
      ORACLE_ALLOW_REMOTE: true
      ORACLE_PASSWORD: oracle

    volumes:
      - ./data:/opt/oracle/oradata
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
CREATE USER developer IDENTIFIED BY password;
GRANT CONNECT TO developer;
GRANT SELECT, INSERT, UPDATE ON books TO developer;
GRANT SELECT, INSERT, UPDATE ON users TO developer;
GRANT SELECT, INSERT, UPDATE ON rent TO developer;
```

```sql
CREATE USER client IDENTIFIED BY password;
GRANT CONNECT TO client;
GRANT SELECT ON books TO client;
GRANT SELECT ON users TO client;
GRANT SELECT ON rent TO client;
```

## Scripts

### TO_DATE FORMAT

Este script permite adaptar los sql mostrados en seed [books y users] de tal manera que adaptan el formato iso al de timestamp de oracle.
El otro fichero (rent) ha sido modificado utilizando atajos de teclado de vscode

```bash
#!/bin/bash

# Definir la ruta del archivo a procesar
archivo="./filename.sql"

# Buscar líneas que contengan una instrucción INSERT INTO
grep "INSERT INTO" "$archivo" | while read linea; do
  # Buscar la cadena de texto que sigue el formato "2020-02-28T07:40:17Z" en la línea actual
  cadena=$(echo "$linea" | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")
  # Si se encontró la cadena de texto, reemplazarla en la línea actual
  if [[ ! -z $cadena ]]; then
    newCadena=$(echo "$cadena" | sed "s/T/ /g" | sed "s/Z//g")
    linea_nueva=$(echo "$linea" | sed "s/$cadena/TO_DATE('$newCadena', 'YYYY-MM-DD HH24:MI:SS')/g")
    echo "$linea_nueva"
  fi
done
```
