import json

# BOOKS
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_BOOKS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('populate/MOCK_DATA_BOOKS.hbase', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    if "'" in dato['autor']:
        dato['autor'] = dato['autor'].replace("'", "''")
    sentencia = "put 'books', '" + dato['codigoInterno'] + "', 'titulo', '" + dato['titulo'] + "'\n"
    sentencia = sentencia + "put 'books', '" + dato['codigoInterno'] + "', 'ISBN', '" + dato['ISBN'] + "'\n"
    sentencia = sentencia + "put 'books', '" + dato['codigoInterno'] + "', 'fechaPublicacion', '" + dato['fechaPublicacion'] + "'\n"
    sentencia = sentencia + "put 'books', '" + dato['codigoInterno'] + "', 'autor', '" + dato['autor'] + "'\n"
    sentencia = sentencia + "put 'books', '" + dato['codigoInterno'] + "', 'edicion', '" + str(dato['edicion']) + "'\n"
    salida.write(sentencia)
salida.close()


# USERS
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_USERS.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('populate/MOCK_DATA_USERS.hbase', 'w')
for dato in datos:
    # Crear la sentencia de inserción
    if "'" in dato['nombre']:
        dato['nombre'] = dato['nombre'].replace("'", "''")
    sentencia = "put 'users', '" + dato['DNI'] + "', 'nombre', '" + dato['nombre'] + "'\n"
    sentencia = sentencia + "put 'users', '" + dato['DNI'] + "', 'fechaNacimiento', '" + dato['fechaNacimiento'] + "'\n"
    sentencia = sentencia + "put 'users', '" + dato['DNI'] + "', 'genero', '" + dato['genero'] + "'\n"
    salida.write(sentencia)
salida.close()


# RENT
# Leer los datos del archivo JSON
with open('../seed/MOCK_DATA_RENT.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
salida = open('populate/MOCK_DATA_RENT.hbase', 'w')
id = 1
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "put 'rent', '" + str(id) + "', 'fecha', '" + dato['fecha'] + "'\n"
    sentencia = sentencia + "put 'rent', '" + str(id) + "', 'fechaDevolucion', '" + dato['fechaDevolucion'] + "'\n"
    sentencia = sentencia + "put 'rent', '" + str(id) + "', 'books', '" + dato['books'] + "'\n"
    sentencia = sentencia + "put 'rent', '" + str(id) + "', 'users', '" + dato['users'] + "'\n"
    salida.write(sentencia)
    id = id + 1
salida.close()

