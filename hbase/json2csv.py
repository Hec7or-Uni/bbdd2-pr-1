import pandas as pd

with open('seed/MOCK_DATA_BOOKS.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('books.csv', encoding='utf-8', index=False)

with open('seed/MOCK_DATA_USERS.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('users.csv', encoding='utf-8', index=False)
