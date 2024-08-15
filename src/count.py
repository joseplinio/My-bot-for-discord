# Importaçoes:
from discord.ext import commands

# Class do comando count:
class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='count')
    async def count (self, ctx):
        await  ctx.send('O contador está em 0')

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Count(bot))