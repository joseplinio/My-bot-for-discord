# Inportaçoes:
from discord.ext import commands
import discord
import json
from discord.ext.commands.errors import CommandNotFound

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
    initial_extensions = ['src.adventure','src.combat','src.inventory','src.count','src.rpg']
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

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = 'geral')
    # Mensage de welcome:
    if channel:
        await channel.send(f'🌟 **Bem-vindo(a) ao {member.guild.name}, {member.mention}!** 🌟\n\n'
                           '🧙‍♂️ **Aventura te chama, bravo(a) aventureiro(a)!** 🧙‍♀️\n\n'
                           '📜 **Antes de começar, confira estas orientações importantes:**\n'
                           '1. **Role dos Jogadores:** Use `/introducao` para se apresentar e conhecer outros aventureiros.\n'
                           '2. **Regras do Reino:** Para garantir a harmonia entre todos os jogadores, leia as regras em #regras-e-diretrizes.\n'
                           '3. **Escolha sua Classe:** Não esqueça de escolher sua classe e raça em #escolha-de-classes.\n'
                           '4. **Inicie sua Jornada:** Assim que estiver pronto(a), vá até #inicio-da-aventura para começar sua primeira missão!\n\n'
                           '⚔️ **Que sua lâmina seja afiada, e seu espírito inabalável. O destino do reino está em suas mãos!** ⚔️')

# Tratamento de erro podendo ser usado em varios casos:
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,CommandNotFound):
        await ctx.send(f'Sorry. comando não reconhecido, caso queira ver a lista de comandos digite "!help". ✨')
        

bot.run(config['token'])