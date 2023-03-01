CREATE 'books', {NAME => 'info'}
CREATE 'users', {NAME => 'info'}
CREATE 'rent', {NAME => 'info'}


-- A continuación, se describen las columnas de cada tabla:
-- Tabla "books":
--     Columna "titulo" - almacenada como una celda con nombre "titulo" en la familia de columnas "info".
--     Columna "ISBN" - almacenada como una celda con nombre "ISBN" en la familia de columnas "info".
--     Columna "fechaPublicacion" - almacenada como una celda con nombre "fechaPublicacion" en la familia de columnas "info".
--     Columna "autor" - almacenada como una celda con nombre "autor" en la familia de columnas "info".
--     Columna "edicion" - almacenada como una celda con nombre "edicion" en la familia de columnas "info".

-- Tabla "users":
--     Columna "nombre" - almacenada como una celda con nombre "nombre" en la familia de columnas "info".
--     Columna "fechaNacimiento" - almacenada como una celda con nombre "fechaNacimiento" en la familia de columnas "info".
--     Columna "genero" - almacenada como una celda con nombre "genero" en la familia de columnas "info".

-- Tabla "rent":
--     Columna "fecha" - almacenada como una celda con nombre "fecha" en la familia de columnas "info".
--     Columna "fechaDevolucion" - almacenada como una celda con nombre "fechaDevolucion" en la familia de columnas "info".
--     Columna "books" - almacenada como una celda con nombre "books" en la familia de columnas "info".
--     Columna "users" - almacenada como una celda con nombre "users" en la familia de columnas "info".