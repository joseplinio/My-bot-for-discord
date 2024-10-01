# Importaçoes:
from discord.ext import commands
import discord
from models.inimigo import Inimigo
from models.player import Player
import random

# Classe dos comandos para o RPG:
class RPGCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.players = {}
        self.batalhas_ativas = {}
    
    @commands.command(name="criar_personagem")
    async def criar_personagem(self, ctx, nome: str, classe: str):
        if ctx.author.id in self.players:
            await ctx.send("Você já tem um personagem. Use !status para ver suas informações.")
        player = Player(nome, 0, 100, 15, [], 0, classe)
        self.players[ctx.author.id] = player
        await ctx.send(f"Personagem {nome} da classe {classe} criado com sucesso!")
    
    @commands.command(name="status")
    async def status(self, ctx):
        pass