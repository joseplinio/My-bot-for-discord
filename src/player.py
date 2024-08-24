# Importaçoes:
from discord.ext import commands
import json
import discord
import asyncio
from src.constants import DEFAULT_HP, DEFAULT_LEVEL, DEFAULT_INVENTORY, DEFAULT_EXP

# Abrindo a confing do arquivo data:
with open('data/config.json') as config_file:
    config = json.load(config_file)

# Permisoes do bot:
intents = discord.Intents.default()
intents.messages = True

# Criação do bot com o prefixo definido
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)


# Class of player:
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='criar_personagem')
    async def create_character(self, ctx,):
        name = await self.pergunta_name(ctx)
        if name:
            user_data = {
                "name": name,
                "level": DEFAULT_LEVEL,
                "life": DEFAULT_LEVEL,
                "inventory": DEFAULT_INVENTORY,
                "exp": DEFAULT_EXP
            }
            with open (f'{ctx.author.id}.json', 'w') as f:
                json.dump(user_data, f)
            await  ctx.send(f'Personagem {name} criado com sucesso!') 
        else:
            await ctx.send('Não foi possível criar o personagem, pois nenhum nome foi fornecido.')
        
    
    async def pergunta_name(self, ctx):
        await ctx.send('Qual vai ser o nome do seu personagem? : ')
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            response = await bot.wait_for('message', check=check,timeout=30.0)
            await ctx.send(f'Ótimo nome,{response.content}!')
            await asyncio.sleep(1.3)
            return response.content        
        except asyncio.TimeoutError:
            await ctx.send('Você demorou muito tempo para responder.')
            return None

    @commands.command(name='view_stats')
    async def view_stats(self, ctx):
        pass  
        
# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Player(bot))