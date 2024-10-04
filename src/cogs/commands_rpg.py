# Importaçoes:
from .cog_player import MetosCriarPersonagem 
from discord.ext import commands
import discord
from src.models.inimigo import Inimigo
from src.models.player import Player
import random
from utils.embed_utils import criar_embed

# Classe dos comandos para o RPG:
class RPGCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.players = {}
        self.batalhas_ativas = {}

    @commands.command()
    async def criar(self, ctx):
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
        player = Player(nome, 1, 100, 15, ["Espada","Ola mundo"], 0, classe)
        self.players[ctx.author.id] = player
        embed =  await criar_embed(
            descriçao=f"**Personagem *{player.nome}* classe *{player.classe}* foi criado com sucesso!**",
            color=discord.Color.purple(),
            campos=[
                ["**[Dica]**", "**Use ``!status`` para ver suas informaçoes.**", True]
            ]
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    async def sta(self, ctx):
        """Mostra o status do personagem do usuário."""
       
        player = self.players.get(ctx.author.id)
        if not player:
            await ctx.send("**Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.**")
            return
        
        embed = await criar_embed(
            titulo=f"Status de {player.nome}",
            color=discord.Color.purple(),
            campos=[
                ["Classe", player.classe, True],
                ["Nível", player.nivel, True],
                ["Experiência",f"{player.exp}/{player._calcular_exp_proximo_nivel():.2f}", True],
                ["Vida", f"{player.vida}/{player.vida_maxima}", True],
                ["Dano", player.dano, True],
                ["Inventário", ", ".join(player.inventario) if player.inventario else "Vazio", False],        
            ]
        )
            
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RPGCommands(bot))