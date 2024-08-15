# Importaçoes:
from discord.ext import commands

# Class de comandos para combate:
class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='combat')
    async def figth (self, ctx):
        id_user = ctx.author.id
        await ctx.send('Você entrou em um combate!')
        
# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Combat(bot))