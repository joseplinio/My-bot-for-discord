# Importações:
from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
import os
import asyncio
import traceback
from utils.interatividade.embeds.embed_utils import criar_embed
from utils.interatividade.funcoes.funcoes_bot import iniciar

# Carega o .env:
load_dotenv()

# Configurar intents:
intents = discord.Intents.default()
intents.message_content = True

# Inicializar o bot:
bot = commands.Bot(command_prefix=os.getenv('PREFIX'), intents=intents)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    
    try:
        channel_id = bot.get_channel(1259652678942720051)
        await iniciar(channel_id)

        print('-'*42)
        print(f'|\033[32m Bot: {bot.user.name} está pronto\033[m!'.center(49))
        print(f'| ID: {bot.user.id}'.center(33))
        print('-'*42)
        print()

    except Exception:
        print(traceback.format_exc())

# Tratamento de erro para comandos inválidos:
@bot.event
async def on_command_error(channel, error):
    if isinstance(error, CommandNotFound):
        await channel.send(f'**Sorry. Comando não reconhecido, caso queira ver a lista de comandos digite `!help`.**')
        
# Função principal para carregar os cogs:
async def load_cogs():
    try:    
        # await bot.load_extension('src.cogs.commands_rpg')
        pass
    except Exception:
        print(traceback.format_exc())

# Iniciar o bot e carregar cogs
async def main():
    async with bot:
        # await load_cogs()
        await bot.start(os.getenv('TOKEN'))

# Executar o bot
asyncio.run(main())
