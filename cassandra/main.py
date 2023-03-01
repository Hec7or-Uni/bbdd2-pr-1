import json


def buscarBook(books, data) -> list:
    i = 0
    while not
    data[i]['codigoInterno']

    return [titulo, autor]


with open('seed/MOCK_DATA_RENT.json', 'r') as rent:
    datosRent = json.load(rent)

    bookList = []
    userList = []

    booksFile = open('../seed/MOCK_DATA_BOOKS.json', 'r')
    datosBooks = json.load(booksFile)
    booksFile.close()

    usersFile = open('../seed/MOCK_DATA_USERS.json', 'r')
    datosUsers = json.load(usersFile)
    usersFile.close()

    for d in datosRent:
        fechaRent = d['fecha']
        fechaDevolucionRent = d['fechaDevolucion']
        booksRent = d['books']
        usersRent = d['users']

        book = {
            "fecha":  fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "titulo":
            "autor":}
        bookList.append(book)

        user = {
            "fecha": fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "nombre":
            "genero":}
        userList.append(user)

with open('seed/MOCK_DATA_RENT_BY_BOOK.json', 'w', encoding='utf-8') as f1:
    json.dump(bookList, f1)
    f1.close()

with open('seed/MOCK_DATA_RENT_BY_USER.json', 'w', encoding='utf-8') as f2:
    json.dump(userList, f2)
    f2.close()

# RENT_BY_BOOK
# Leer los datos del archivo JSON
with open('seed/MOCK_DATA_RENT_BY_BOOK.json', 'r') as archivo:
    datos = json.load(archivo)

with open('MOCK_DATA_RENT_BY_BOOK.cql', 'w') as salida:
    # Generar las sentencias de inserción
    for dato in datos:
        # Crear la sentencia de inserción
        sentencia = "INSERT INTO rent_by_book (fecha, fechaDevolucion, books, users, titulo, autor) VALUES ({dato['fecha']}, '{dato['fechaDevolucion']}', {dato['books']}, {dato['users']}, {dato['titulo']}, {dato['autor']})"
        salida.write(sentencia)


# RENT_BY_USER
# Leer los datos del archivo JSON
with open('seed/MOCK_DATA_RENT_BY_USER.json', 'r') as archivo:
    datos = json.load(archivo)

# Generar las sentencias de inserción
for dato in datos:
    # Crear la sentencia de inserción
    sentencia = "INSERT INTO rent_by_user (fecha, fechaDevolucion, books, users, nombre, genero) VALUES ({dato['fecha']}, '{dato['fechaDevolucion']}', {dato['books']}, {dato['users']}, {dato['nombre']}, {dato['genero']})"
