# Importaçoes:
import sqlite3
from discord.ext import commands

# Funçao para um desafio da Sofia sobre database
# Inicia o databese e usa dois parametros (id_user, count):

def init_db(id_user, count):
    global banco
    banco = sqlite3.connect(':memory:')
    cursor = banco.cursor()
    cursor.execute("create table logins(id_user  INTEGER,chamadas INTEGER)")
    cursor.execute("insert into logins values (?, ?)", (id_user, count))
    banco.commit()
    for c in cursor.execute("select * from logins"):
        print(c)
    banco.close()

def check(ctx, m):
    return m.author == ctx.author and m.channel == ctx.channel


async def create_user(ctx, id, count):
    if check == check:
        count += 1    
    id_user = ctx.author.id
    id = id_user
    

def get_user():

    