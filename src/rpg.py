# Importaçao
from discord.ext import commands
import json
import discord

# Carregar configurações:
with open('data/config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Cogs para o jogo
class Rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='criar_user')
    async def cria_user(self, ctx):
        pass
    
    def cria_monstro(self):
        level = 2
        monstro = {
            "nome":"Mostro",
            "lv": level,
            "dano": level * 2,
            "hp":level * 3.5
        }
        return monstro    
    

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Rpg(bot)) 