# Importaçoes:
import sqlite3

# Banco de dodos global
banco = sqlite3.connect('./data/database.db')

# Funçao para um desafio da Sofia sobre database
def create_user():
    global banco
    cursor = banco.cursor()
    cursor.execute("create table logins (id_user INTEGER, chamadas INTEGER)")
    banco.commit()

# Adiciona um usuario no banco de dados:
def add_user(user_id, count):
    global banco
    cursor = banco.cursor()
    cursor.execute("insert into logins values (?,?)", (user_id, count))
    banco.commit()

# Pega o ID de um usuario no banco de dados:
def get_user(user_id):
    global banco
    cursor = banco.cursor()
    cursor.execute('select * from logins where id = ?',(user_id))
    user = cursor.fetchone([0])
    return user

# Incrementa o contador do usuario aqui:
def inc_user(id):
    pass

add_user(123,10)
users = get_user()
for user in users:
    print(user)
