import random
import datetime
import json

# Definir el rango de fechas para generar una fecha aleatoria
fecha_inicio = datetime.datetime(2020, 1, 1, 0, 0, 0)
fecha_final = datetime.datetime(2023, 1, 1, 0, 0, 0)


def getDates() -> list:
    return []


with open('seed/MOCK_DATA_BOOKS.json', encoding='utf-8') as f1:
    books = json.load(f1)
    f1.close()

with open('seed/MOCK_DATA_USERS.json', encoding='utf-8') as f2:
    users = json.load(f2)
    f2.close()
    print(users)

rentList = []
for i in range(0, 100):
    rent = {
        "fecha": "",
        "fechaDevolucion": "",
        "books": books[i]["codigoInterno"],
        "users": users[i]["DNI"]
    }
    rentList.append(rent)

print(rentList)
