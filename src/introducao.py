# importaçoes:
from discord.ext import commands

# Comandos para o bot:
class Introducao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando introduçao com a funçao de instruir o user:
    @commands.command(name='introducao')
    async def explore(self, ctx):
        await ctx.send("👋 **Bem-vindo ao RPG Bot!**\n\n"
            "Aqui estão algumas dicas para começar sua aventura:\n"
            "1. Use `/iniciar_jornada` no canal de comandos para criar seu personagem.\n"
            "Prepare-se para uma jornada épica!")

# Define os comandos para o bot:
async def setup(bot):
     await bot.add_cog(Introducao(bot))