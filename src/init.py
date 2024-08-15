# Importaçao
from discord.ext import commands
from cogs import rpg

# Cogs para o jogo
class Init(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='init_rpg')
    async def init_rpg(self, ctx):
        await ctx.send(rpg)
