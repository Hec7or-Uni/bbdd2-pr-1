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
   fechaNacimiento  TIMESTAMP       NOT NULL,
   DNI              VARCHAR(10)     PRIMARY KEY,
   genero           VARCHAR(6)      NOT NULL
);

CREATE TABLE rent (
   fecha            TIMESTAMP       NOT NULL,
   fechaDevolucion  TIMESTAMP       NOT NULL,
   books            VARCHAR(36),
   users            INT,
   PRIMARY KEY (books, users, fecha),
   FOREIGN KEY (books) REFERENCES books(codigoInterno),
   FOREIGN KEY (users) REFERENCES users(DNI)
);
