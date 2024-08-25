# Importaçoes:
from discord.ext import commands
from src.player import Player

# Class do comando count:
class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player_cog = Player(bot)

    # Comanmdo que mandar um mensage para o user sobre o inicio do RPG:
    commands.command(name='iniciar_jornada')
    async def start_adventure(ctx):
        await ctx.send(f'*{ctx.author.name}* **iniciou uma aventura!**')



# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Count(bot))