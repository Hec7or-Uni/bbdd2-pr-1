import json


def buscarBook(book, data, librosVisitados) -> list:
    i = 0
    encontrado = False
    titulo = ""
    autor = ""
    while (not encontrado):
        if not i in librosVisitados:
            dato = data[i]
            if dato["codigoInterno"] == book:
                encontrado = True
                titulo = dato["titulo"]
                autor = dato["autor"]
                librosVisitados.add(i)
        i = i + 1
    return [titulo, autor]


def buscarUser(user, data, usuariosVisitados) -> list:
    i = 0
    encontrado = False
    nombre = ""
    genero = ""
    while (not encontrado):
        if not i in usuariosVisitados:
            dato = data[i]
            if dato["DNI"] == user:
                encontrado = True
                nombre = dato["nombre"]
                genero = dato["genero"]
                usuariosVisitados.add(i)
        i = i + 1
    return [nombre, genero]


with open('../seed/MOCK_DATA_RENT.json', 'r') as rent:
    datosRent = json.load(rent)

    librosVisitados = set()
    usuariosVisitados = set()

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

        tituloAutor = buscarBook(booksRent, datosBooks, librosVisitados)
        nombreGenero = buscarUser(usersRent, datosUsers, usuariosVisitados)

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

with open('../seed/MOCK_DATA_RENT_BY_BOOK.json', 'w', encoding='utf-8') as f1:
    json_content = json.dumps(bookList, indent=4)
    f1.write(json_content)
    f1.close()

with open('../seed/MOCK_DATA_RENT_BY_USER.json', 'w', encoding='utf-8') as f2:
    json_content = json.dumps(userList, indent=4)
    f2.write(json_content)
    f2.close()