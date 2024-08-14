# Importaçao
from discord.ext import commands
from random import randint

# Cogs para o jogo
class Init(commands.cog):
    def __init__(self, bot):
        self.bot = bot
