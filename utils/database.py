# Importaçao:
import sqlite3

# Banco de dodos global
banco = sqlite3.connect('./data/database.db')

# Funçao para um desafio da Sofia sobre database:
def create_user():
    global banco
    cursor = banco.cursor()
    cursor.execute("create table if not exists logins (user_id INTEGER, chamadas INTEGER)")
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
    cursor.execute("select * from logins where user_id = ?",(user_id,))
    user = cursor.fetchone()
    return user

# Incrementa o contador do usuario aqui:
def inc_user(user_id):
    global banco
    cursor = banco.cursor()
    # Pega as chamadas de cada ID:
    cursor.execute("select chamadas from logins where user_id = ?",(user_id,))
    result = cursor.fetchone()
    # Se o user nao existir:
    if result is None:
        cursor.execute("insert into logins values (?,?)",(user_id,0))
    # Se existir:
    else:
        chamadas_atuais = result[0] + 1
        cursor.execute("update logins set chamadas = ? where user_id = ?",(chamadas_atuais, user_id))
    # Salva as alteraçoes:
    banco.commit()
    # Retorna a contagems:
    cursor.execute("select user_id, chamadas from logins where user_id = ?",(user_id,))
    return cursor.fetchone()
