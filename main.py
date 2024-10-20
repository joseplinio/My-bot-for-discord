# Importações:
from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
import os
import asyncio
import traceback
from src.cogs.botes_interaction import BotesForRpg
from utils.embed_utils import criar_embed

# Carega o .env:
load_dotenv()

# Configurar intents:
intents = discord.Intents.default()
intents.message_content = True

# Inicializar o bot:
bot = commands.Bot(command_prefix=os.getenv('PREFIX'), intents=intents)

# Funçao para iniciar o bot com mensage para o user:
async def iniciar(channel):
        """Usado para inicar o jogo"""
        try:

            await channel.send(embed=criar_embed(
                color=discord.Color.dark_green(),
                imagem="https://i.pinimg.com/originals/55/6e/42/556e42e20bd1da172be9b448239a68dd.gif"
            ))
            
            await channel.send(embed=criar_embed(
                titulo="🌟 **Bem-vindo(a) ao Mundo de Aventuras!** 🌟\n\n",
                color=discord.Color.dark_green(),
                descricao="Prepare-se para embarcar em uma jornada épica de batalhas, descobertas e evolu'ção! ⚔️🛡️\n"
                    "Crie seu personagem, usando `Criar Personagem`!\n\n"
                    "Que as estrelas guiem o seu caminho, e a sorte esteja sempre ao seu lado! 🍀✨\n\n",
                ),
                view=BotesForRpg(bot)
            )

        except Exception:
            print(traceback.format_exc())

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
async def on_command_error(channel, error):
    if isinstance(error, CommandNotFound):
        await channel.send(f'**Sorry. Comando não reconhecido, caso queira ver a lista de comandos digite `!help`.**')
        
# Função principal para carregar os cogs:
async def load_cogs():
    try:    
        await bot.load_extension('src.cogs.commands_rpg')
    except Exception:
        print(traceback.format_exc())

# Iniciar o bot e carregar cogs
async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('TOKEN'))

# Executar o bot
asyncio.run(main())
