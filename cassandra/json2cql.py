import json


# BOOKS
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_BOOKS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('MOCK_DATA_BOOKS.cql', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "INSERT INTO practice1.books (titulo, codigoInterno, ISBN, fechaPublicacion, autor, edicion) VALUES ('" + dato['titulo'] + "', '" + dato['codigoInterno'] + "', '" + dato['ISBN'] + "', '" + dato['fechaPublicacion'] + "', '" + dato['autor'] + "', " + str(dato['edicion']) + ");\n"
    salida.write(sentencia)
salida.close()


# USERS
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_USERS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('MOCK_DATA_USERS.cql', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "INSERT INTO practice1.users (nombre, fechaNacimiento, DNI, genero) VALUES (" + dato['nombre'] + ", " + dato['fechaNacimiento'] + ", " + dato['DNI'] + ", " + dato['genero'] + ");\n"
    salida.write(sentencia)
salida.close()


# RENT_BY_BOOK
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_RENT_BY_BOOK.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('MOCK_DATA_RENT_BY_BOOK.cql', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "INSERT INTO practice1.rent_by_book (fecha, fechaDevolucion, books, users, titulo, autor) VALUES (" + dato['fecha'] + ", " + dato['fechaDevolucion'] + ", " + dato['books'] + ", " + dato['users'] + ", " + dato['titulo'] + ", " + dato['autor'] + ");\n"
    salida.write(sentencia)
salida.close()


# RENT_BY_USER
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_RENT_BY_USER.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('MOCK_DATA_RENT_BY_USER.cql', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "INSERT INTO practice1.rent_by_user (fecha, fechaDevolucion, books, users, nombre, genero) VALUES (dato['fecha'], " + dato['fechaDevolucion'] + ", " + dato['books'] + ", " + dato['users'] + ", " + dato['nombre'] + ", " + dato['genero'] + ");\n"
    salida.write(sentencia)
salida.close()
