import json


def buscarBook(book, data) -> list:
    i = 0
    encontrado = False
    titulo = ""
    autor = ""
    while not encontrado:
        id = data[i]["codigoInterno"]
        if id == book:
            encontrado = True
            titulo = data[i]["titulo"]
            autor = data[i]["autor"]
        else:
            if id == 999:
                encontrado = True
    return [titulo, autor]


def buscarUser(user, data) -> list:
    i = 0
    encontrado = False
    nombre = ""
    genero = ""
    while not encontrado:
        id = data[i]["DNI"]
        if id == book:
            encontrado = True
            nombre = data[i]["nombre"]
            genero = data[i]["genero"]
        else:
            if id == 999:
                encontrado = True
    return [nombre, genero]


with open('seed/MOCK_DATA_RENT.json', 'r') as rent:
    datosRent = json.load(rent)

    bookList = []
    userList = []

    booksFile = open('seed/MOCK_DATA_BOOKS.json', 'r')
    datosBooks = json.load(booksFile)
    booksFile.close()

    usersFile = open('seed/MOCK_DATA_USERS.json', 'r')
    datosUsers = json.load(usersFile)
    usersFile.close()

    for d in datosRent:
        fechaRent = d['fecha']
        fechaDevolucionRent = d['fechaDevolucion']
        booksRent = d['books']
        usersRent = d['users']

        tituloAutor = buscarBook(booksRent, datosBooks)
        nombreGenero = buscarUser(usersRent, datosUsers)

        book = {
            "fecha":  fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "titulo": tituloAutor[0],
            "autor": tituloAutor[1]}
        bookList.append(book)

        user = {
            "fecha": fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "nombre": nombreGenero[0],
            "genero": nombreGenero[1]}
        userList.append(user)

with open('seed/MOCK_DATA_RENT_BY_BOOK.json', 'w', encoding='utf-8') as f1:
    json.dump(bookList, f1)
    f1.close()

with open('seed/MOCK_DATA_RENT_BY_USER.json', 'w', encoding='utf-8') as f2:
    json.dump(userList, f2)
    f2.close()

with open('seed/MOCK_DATA_RENT.json', 'r') as rent:
    datosRent = json.load(rent)

    bookList = []
    userList = []

    booksFile = open('seed/MOCK_DATA_BOOKS.json', 'r')
    datosBooks = json.load(booksFile)
    booksFile.close()

    usersFile = open('seed/MOCK_DATA_USERS.json', 'r')
    datosUsers = json.load(usersFile)
    usersFile.close()

    for d in datosRent:
        fechaRent = d['fecha']
        fechaDevolucionRent = d['fechaDevolucion']
        booksRent = d['books']
        usersRent = d['users']

        tituloAutor = buscarBook(booksRent, datosBooks)
        nombreGenero = buscarUser(usersRent, datosUsers)

        book = {
            "fecha":  fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "titulo": tituloAutor[0],
            "autor": tituloAutor[1]}
        bookList.append(book)

        user = {
            "fecha": fechaRent,
            "fechaDevolucion": fechaDevolucionRent,
            "books": booksRent,
            "users": usersRent,
            "nombre": nombreGenero[0],
            "genero": nombreGenero[1]}
        userList.append(user)

with open('seed/MOCK_DATA_RENT_BY_BOOK.json', 'w', encoding='utf-8') as f1:
    json.dump(bookList, f1)
    f1.close()

with open('seed/MOCK_DATA_RENT_BY_USER.json', 'w', encoding='utf-8') as f2:
    json.dump(userList, f2)
    f2.close()
