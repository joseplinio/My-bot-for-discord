# Importaçoes:
from discord.ext import commands
from json_handler import load_data, save_data

# Class do comando count:
class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add_item')
    async def count (self, ctx, item: str):
        user_data = load_data(f'{ctx.author.id}.json')
        user_data['inventory'].append(item)
        save_data(f'{ctx.author.id}.json', user_data)        
        await  ctx.send(f'O item {item} foi adicionado com sucesso ao seu inventário.')


    @commands.command(name='ver_inventory')
    async def count (self, ctx):
        user_data = load_data(f'{ctx.author.id}.json')
        inventory = user_data.get('inventory', [])
        await ctx.send(f'Seu inventário: {", ".join(inventory)}')


# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Inventory(bot))