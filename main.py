# Inportaçoes:
from discord.ext import commands
import discord
import json



# Carregar configurações:
with open('data/config.json') as config_file:
    config = json.load(config_file)

# Configurar intents:
intents = discord.Intents.default()
intents.message_content = True
        
# Inicializar o bot:
bot = commands.Bot(command_prefix = config['prefix'], intents = intents)

# Trazendo os comandos para a main ;] :
async def load_extensions():
    initial_extensions = ['src.adventure','src.combat','src.inventory','src.count']
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'\t\033[32mSrc \033[m{extension}\033[32m carregada com sucesso\033[m!')
        except Exception as e:
            print(f'\033[31mErro ao carregar a cog {extension}: {e}\033[m') 

# Mensagem de confirmação:
@bot.event
async def on_ready():
    await load_extensions() # Carrega as Cogs
    print()
    print('-'*42)
    print(f'|\033[32m Bot: {bot.user.name} está pronto\033[m!'.center(49))
    print(f'| ID: {bot.user.id}'.center(33))
    print('-'*42)


# Inicia o banco de dados
# Db is here.

# Iniciar o bot
bot.run(config['token'])