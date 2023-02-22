CREATE TABLE books (
   titulo           VARCHAR(255)    NOT NULL,
   codigoInterno    UUID            PRIMARY KEY,
   ISBN             VARCHAR(10)     NOT NULL,
   fechaPublicacion TIMESTAMP       NOT NULL,
   autor            VARCHAR(255)    NOT NULL,
   edicion          INT             NOT NULL
);

CREATE TABLE users (
   nombre           VARCHAR(255)    NOT NULL,
   fechaNaciemiento TIMESTAMP       NOT NULL,
   DNI              INT             PRIMARY KEY,
   genero           VARCHAR(6)      NOT NULL
);

CREATE TABLE rent (
   fecha            TIMESTAMP       NOT NULL,
   fechaDevolucion  TIMESTAMP       NOT NULL,
   books            UUID            NOT NULL,
   users            INT             NOT NULL,
   PRIMARY KEY (books, users, fecha),
   FOREIGN KEY (books) REFERENCES books(codigoInterno),
   FOREIGN KEY (users) REFERENCES users(DNI)
);
