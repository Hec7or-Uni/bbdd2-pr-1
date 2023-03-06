CREATE TABLE books (
   titulo           VARCHAR(255)    NOT NULL,
   codigoInterno    VARCHAR(36)     PRIMARY KEY,
   ISBN             VARCHAR(13)     NOT NULL,
   fechaPublicacion TIMESTAMP       NOT NULL,
   autor            VARCHAR(255)    NOT NULL,
   edicion          INT             NOT NULL
);

CREATE TABLE users (
   nombre           VARCHAR(255)    NOT NULL,
   fechaNaciemiento TIMESTAMP       NOT NULL,
   DNI              VARCHAR(9)      PRIMARY KEY,
   genero           VARCHAR(6)      NOT NULL
);

CREATE TABLE rent (
   books            VARCHAR(36),
   users            VARCHAR(9),
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP       NOT NULL,
   PRIMARY KEY (books, users, fecha),
   FOREIGN KEY (books) REFERENCES books(codigoInterno),
   FOREIGN KEY (users) REFERENCES users(DNI)
);
