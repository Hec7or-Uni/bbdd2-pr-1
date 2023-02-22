import json


# BOOKS
# Leer los datos del archivo JSON
with open('MOCK_DATA_BOOKS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = f"INSERT INTO books (titulo, codigoInterno, ISBN, fechaPublicacion, autor, edicion) VALUES ({dato['titulo']}, '{dato['codigoInterno']}', {dato['ISBN']}, {dato['fechaPublicacion']}, {dato['autor']}, {dato['edicion']})"


# USERS
# Leer los datos del archivo JSON
with open('MOCK_DATA_USERS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = f"INSERT INTO users (nombre, fechaNacimiento, DNI, genero) VALUES ({dato['nombre']}, '{dato['fechaNacimiento']}', {dato['DNI']}, {dato['genero']})"


# RENT_BY_BOOK
# Leer los datos del archivo JSON
with open('MOCK_DATA_RENT_BY_BOOK.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = f"INSERT INTO rent_by_book (fecha, fechaDevolucion, books, users, titulo, autor) VALUES ({dato['fecha']}, '{dato['fechaDevolucion']}', {dato['books']}, {dato['users']}, {dato['titulo']}, {dato['autor']})"


# RENT_BY_USER
# Leer los datos del archivo JSON
with open('MOCK_DATA_RENT_BY_USER.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = f"INSERT INTO rent_by_user (fecha, fechaDevolucion, books, users, nombre, genero) VALUES ({dato['fecha']}, '{dato['fechaDevolucion']}', {dato['books']}, {dato['users']}, {dato['nombre']}, {dato['genero']})"
