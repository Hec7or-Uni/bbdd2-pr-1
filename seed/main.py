import random
import datetime
import json


def getDates() -> list:
    year = random.randint(2000, 2020)
    month = random.randint(1, 12)
    day, offset = random.randint(1, 15), random.randint(1, 13)
    hour1, hour2 = random.randint(8, 20), random.randint(8, 20)
    minutes1, minutes2 = random.randint(0, 59), random.randint(0, 59)
    secs1, secs2 = random.randint(0, 59),  random.randint(0, 59)
    fecha_inicio = datetime.datetime(year, month, day, hour1, minutes1, secs1)
    fecha_final = datetime.datetime(
        year, month, day+offset, hour2, minutes2, secs2)

    return [str(fecha_inicio), str(fecha_final)]


with open('seed/MOCK_DATA_BOOKS.json', encoding='utf-8') as f1:
    books = json.load(f1)
    f1.close()

with open('seed/MOCK_DATA_USERS.json', encoding='utf-8') as f2:
    users = json.load(f2)
    f2.close()

rentList = []
for i in range(0, 100):
    dates = getDates()
    # print(dates)
    rent = {
        "fecha":  dates[0],
        "fechaDevolucion": dates[1],
        "books": books[i]["codigoInterno"],
        "users": users[i]["DNI"]
    }
    rentList.append(rent)

with open('seed/MOCK_DATA_RENT.json', 'w', encoding='utf-8') as f3:
    json.dump(rentList, f3)
    f3.close()
