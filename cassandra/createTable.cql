CREATE KEYSPACE practice1 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE practice1.books (
   titulo           TEXT,
   codigoInterno    TEXT,
   ISBN             TEXT,
   fechaPublicacion TIMESTAMP,
   autor            TEXT,
   edicion          INT,
   PRIMARY KEY (codigoInterno)
);

CREATE TABLE practice1.users (
   nombre           TEXT,
   fechaNacimiento TIMESTAMP,
   DNI              TEXT,
   genero           TEXT,
   PRIMARY KEY (DNI)
);

CREATE TABLE practice1.rent_by_book (
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP,
   books            TEXT,
   users            TEXT,
   titulo           TEXT,
   autor            TEXT,
   PRIMARY KEY (books, users, fecha)
);

CREATE TABLE practice1.rent_by_user (
   fecha            TIMESTAMP,
   fechaDevolucion  TIMESTAMP,
   books            TEXT,
   users            TEXT,
   nombre           TEXT,
   genero           TEXT,
   PRIMARY KEY (users, books, fecha)
);

-- En este diseño, se crean dos tablas "rent_by_book" y "rent_by_user" para denormalizar los datos de la tabla "rent". Cada tabla tiene una clave primaria compuesta formada por las columnas "books", "users" y "fecha", lo que garantiza que cada fila en la tabla sea única y se pueda acceder de manera eficiente utilizando estas columnas.
-- Para facilitar la búsqueda de datos en las tablas "rent_by_book" y "rent_by_user", se duplican los datos de las tablas "books" y "users". Por ejemplo, en la tabla "rent_by_book", se agregan las columnas "titulo" y "autor" para que sea más fácil encontrar información sobre el libro prestado.
-- Es importante tener en cuenta que este diseño se adapta a un caso de uso específico y podría requerir ajustes según las necesidades de la aplicación.
