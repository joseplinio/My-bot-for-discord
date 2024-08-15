# Importaçoes:
from discord.ext import commands
from src import rpg

# Class de inicialisaçao do jogo:
class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='init_rpg')
    async def init_rpg(self, ctx):
        await ctx.send(rpg)
