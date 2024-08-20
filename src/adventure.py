# importaçoes:
from discord.ext import commands

# Comandos para o bot:
class Adventure(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando explorar com a funçao de começar a exploraçao:
    @commands.command(name='explorar')
    async def explore(self, ctx):
        await ctx.send('Você está explorando uma área desconhecida...')

# Define os comandos para o bot:
async def setup(bot):
     await bot.add_cog(Adventure(bot))