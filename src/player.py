# Importaçoes:
from discord.ext import commands
import json

# Class of player:
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='criar_personagem')
    async def create_character(self, ctx, name = str):
        user_data = {
            "name": name,
            "level": 1,
            "life": 100,
            "inventory": [],
            "exp": 0
        }
        with open (f'{ctx.author.id}.json', 'w') as f:
            json.dump(user_data, f)
        await  ctx.send(f'Personagem {name} criado com sucesso!')

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Player(bot))