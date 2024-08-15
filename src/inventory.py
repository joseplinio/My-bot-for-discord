# Importaçoes
from discord.ext import commands

# Comandos
class Inventory(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot
        self.items = {}

    # Adicionar item
    @commands.command(name='add_item')
    async def inventory(self, ctx, item: str):
        user = ctx.author.id
        if user not in self.items:
            self.items[user] = []
        self.items[user].append(item)
        await ctx.send(f'Item {item} adicionado ao inventário!')
    
    # Mostra iventario
    @commands.command(name='show_inventory')
    async def show_inventory(self, ctx):
        user = ctx.author.id
        items = self.items.get('user' ,[])
        await ctx.send(f'Your inventory: {', '.join(items)}')

async def setup(bot):
     await bot.add_cog(Inventory(bot))