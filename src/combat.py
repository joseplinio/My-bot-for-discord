# importaçoes:
from discord.ext import commands
from constants import DEFAULT_HP

# Comandos para o bot:
class Battles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Battles(bot))