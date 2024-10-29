# Importações:
from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
import os
import asyncio
import traceback
from utils.interatividade.funcoes_for_bot.msg_init import iniciar

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
        channel_id = 1259652678942720051  # ID do canal que você deseja acessar
        channel = bot.get_channel(channel_id)
        
        if channel:
            await iniciar(channel, bot)  # Inicializa a lógica do bot com o canal

        # Log de inicialização do bot
        print('-' * 42)
        print(f'|\033[32m Bot: {bot.user.name} está pronto\033[m!'.center(49))
        print(f'| ID: {bot.user.id}'.center(33))
        print('-' * 42)
        print()

    except Exception as e:
        print(f"Ocorreu um erro no evento on_ready: {e}")
        print(traceback.format_exc())

# Tratamento de erro para comandos inválidos:
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'**Sorry. Comando não reconhecido, caso queira ver a lista de comandos digite `!help`.**')
        
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
