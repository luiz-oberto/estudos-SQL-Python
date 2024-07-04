# AULA 388, 389, 390, 391, 392, 393, 394, 
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# # CUIDADO: fazendo DELETE sem WHERE
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# connection.commit()
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# connection.commit()

# # SQL
# # # cria a tabela
# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'name TEXT,'
#     'weight REAL'
#     ')'
# )
# connection.commit()

# # Registrar valores nas colunas da tabela
# # CUIDADO: sql injection
# sql = (
#     f'INSERT INTO {TABLE_NAME} ' 
#     '(name, weight) '
#     'VALUES '
#     '(:name, :weight)'
# )

# # # executa uma única requisição
# # cursor.execute(sql, ['Joana', 4])

# # # executa muitas querys
# # cursor.executemany(
# #     sql,
# #     (
# #         ('Joana', 4), ('Luiz', 5)
# #     ) 
# # )

# # # Executando com dicionários
# cursor.execute(sql, {'name': 'sem nome', 'weight': 4.5})
# cursor.executemany(sql, (
#     {'name': 'Joãozinho', 'weight': 3},
#     {'name': 'Maria', 'weight': 4},
#     {'name': 'Helena', 'weight': 2},
#     {'name': 'Joana', 'weight': 4.5},
# ))
# connection.commit()
# print(sql)

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)