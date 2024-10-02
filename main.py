# Importações:
from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
import os
import asyncio

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
    print()
    print('-'*42)
    print(f'|\033[32m Bot: {bot.user.name} está pronto\033[m!'.center(49))
    print(f'| ID: {bot.user.id}'.center(33))
    print('-'*42)

# Evento de boas-vindas a novos membros:
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='geral')
    # Mensagem de welcome:
    if channel:
        await channel.send(f'🌟 **Bem-vindo(a) ao {member.guild.name}, {member.mention}!** 🌟\n\n'
                           '🧙‍♂️ **Aventura te chama, bravo(a) aventureiro(a)!** 🧙‍♀️\n\n'
                           '1. **Role dos Jogadores:** Use `/introducao` para aprender como começar sua jornada.\n'
                           '⚔️ **Que sua lâmina seja afiada, e seu espírito inabalável. O destino do reino está em suas mãos!** ⚔️')

# Tratamento de erro para comandos inválidos:
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'**Sorry. Comando não reconhecido, caso queira ver a lista de comandos digite `!help`.**')

# Função principal para carregar os cogs:
async def load_cogs():
    try:
        await bot.load_extension('src.cogs.commands_rpg')
    except Exception as e:
        print(f"Erro ao carregar cogs: {e}")
 
# Iniciar o bot e carregar cogs
async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('TOKEN'))

# Executar o bot
asyncio.run(main())
