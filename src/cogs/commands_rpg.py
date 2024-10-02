# Importaçoes:
from .cog_player import CriarPersonagem 
from discord.ext import commands
import discord
from src.models.inimigo import Inimigo
from src.models.player import Player
import random

# Classe dos comandos para o RPG:
class RPGCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.players = {}
        self.batalhas_ativas = {}
    
    @commands.command(name="criar_personagem")
    async def criar_personagem(self, ctx):
        if ctx.author.id in self.players:
            await ctx.send("**Você já tem um personagem. Use `!status` para ver suas informações.**")
            return
        
        # Instancia a classe CriarPersonagem para usar as perguntas:
        criando_personagem = CriarPersonagem(self.bot)

        # Pergunta o nome e a classe:

        nome = await criando_personagem.pergunta_nome(ctx)
        if not nome:
            await ctx.send("**Criação de personagem cancelada.**")
            return
        

        classe = await criando_personagem.pergunta_classe(ctx)
        if not classe:
            await ctx.send("**Criação de personagem cancelada.**")
            return
        
        # Cria o personagem:
        player = Player(nome, 0, 100, 15, [], 0, classe)
        self.players[ctx.author.id] = player
        await ctx.send(f"**Personagem ***{nome}*** da classe ***{classe}*** criado com sucesso!**")
    
async def setup(bot):
    await bot.add_cog(RPGCommands(bot))
