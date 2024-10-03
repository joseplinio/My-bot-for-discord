# Importaçoes:
from .cog_player import MetosCriarPersonagem 
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
    
    @commands.command()
    async def criar_personagem(self, ctx):
        """Cria o personagem para o jogo."""
        if ctx.author.id in self.players:
            await ctx.send("**Você já tem um personagem. Use ``!status`` para ver suas informações.**")
            return
        
        # Instancia a classe CriarPersonagem para usar as perguntas:
        criando_personagem = MetosCriarPersonagem(self.bot)

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
        player = Player(nome, 1, 100, 15, [], 0, classe)
        self.players[ctx.author.id] = player
        await ctx.send(f"**Personagem __*{nome}*__ da classe __*{classe}*__ criado com sucesso!**")

    @commands.command()
    async def status(self, ctx):
        """Mostra o status do personagem do usuário."""
       
        player = self.players.get(ctx.author.id)
        if not player:
            await ctx.send("Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.")
            return
        
        embed = discord.Embed(title=f"Status de {player.nome}", color= discord.Color.purple())
        embed.add_field(name="Classe", value=player.classe, inline=True)
        embed.add_field(name="Nível", value=player.nivel, inline=True)
        embed.add_field(name="Experiência", value=f"{player.exp}/{player._calcular_exp_proximo_nivel()}", inline=True)
        embed.add_field(name="Vida", value=f"{player.vida}/{player.vida_maxima}", inline=True)
        embed.add_field(name="Dano", value=player.dano, inline=True)
        embed.add_field(name="Inventário", value= ", ".join(player.inventario) if player.inventario else "Vazio", inline=False)      
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RPGCommands(bot))