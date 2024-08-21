# Importaçoes:
from discord.ext import commands
import asyncio

# Cogs para o jogo
class Rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='criar_personagem')
    async def create_user(self, ctx, hp: float = 100, lv: int = 1 , exp: float = 0):
        # Pergunta para o nome do personagem ao user:
        await ctx.send('Qual vai ser o nome do seu personagem? : ')
        
        # Cheka quem mandou a mensagem e o canal que mandou
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            # Debug: Verificando se o bot está esperando pela resposta
            response = await self.bot.wait_for("message",check=check,timeout=30.0)

            # Responde o user:   
            await ctx.send(f'Ótimo nome, **{response.content}!**')
            
            # Faz esperar a mensagem do bot de forma assíncrona:
            await asyncio.sleep(1.5)

            # Mostra os stats do user depois de criar o player:
            await ctx.send(f"""```
- |Seus Status|
``` **Vida**: {hp}, **Lv**: {lv}, **Exp**: {exp}""")
        # Debug: O tempo acabou:
        except asyncio.TimeoutError:
            await ctx.send('Voce demorou muito tempo para responder.')

    
    def cria_monstro(self):
        level = 2
        monstro = {
            "nome":"Mostro",
            "lv": level,
            "dano": level * 2,
            "hp":level * 3.5
        }
        return monstro    
    

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Rpg(bot)) 