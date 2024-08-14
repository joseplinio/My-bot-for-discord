# importaçoes
from discord.ext import commands
import json

# Abre a chave da api com json
with open('data/config.json') as config_file:
     config = json.load(config_file)
     api_key = config.get('api_key')

# Comandos para o bot
class Adventure(commands.Cog):
    def __init__(self, bot):
         self.bot = bot

    @commands.command(name='explorar')
    async def explore(self, ctx):
         await ctx.send('Você está explorando uma área desconhecida...')

# Define os comandos para o bot
async def setup(bot):
     await bot.add_cog(Adventure(bot))