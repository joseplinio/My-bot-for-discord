from discord.ext import commands
import json

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='combat')
    async def figth (self, ctx):
        await ctx.send('Você entrou em um combate!')

async def setup(bot):
    await bot.add_cog(Combat(bot))