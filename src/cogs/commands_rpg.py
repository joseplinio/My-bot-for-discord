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
    async def c(self, ctx):
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
        embed = criar_embed(
            descricao=f"**Personagem *{player.nome}* classe *{player.classe}* foi criado com sucesso!**",
            color=discord.Color.purple(),
            campos=[
                ["**[Dica]**", "**Use ``!status`` para ver suas informaçoes.**", True]
            ]
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx):
        """Mostra o status do personagem do usuário."""
       
        player = self.players.get(ctx.author.id)
        if not player:
            await ctx.send("**Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.**")
            return
        
        embed = criar_embed(
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
            
    @commands.command()
    async def lutar(self, ctx):
        """Inicia uma luta contra um inimigo aleatório."""
        try:
            player = self.players.get(ctx.author.id)
        
            if not player:
                await ctx.send("**Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.**")
                return
            
            if ctx.author.id in self.batalhas_ativas:
                await ctx.send("**Você já está em uma batalha!**")
                return
            
            inimigo = Inimigo("Dragao", random.randint(100, 120), random.randint(15, 20), 50)
            self.batalhas_ativas[ctx.author.id] = inimigo

            inicio_batlha = criar_embed(
                titulo="Batalha Iniciada!",
                descricao=f"Voce encontrou o {inimigo.nome}\n{inimigo.descricao}",
                color= discord.Color.purple(),
                campos=[
                    ["Vida do Inimigo", inimigo.vida, True],
                    ["Sua vida", f"{player.vida}/{player.vida_maxima}", True],
                    ["Comando", "Use !atacar para atacar o inimigo ou !fugir para tentar escapar.", False]
                ]
            )

            await ctx.send(embed=inicio_batlha)

        except Exception as e:
            print(f"ERRO: {e}")

    @commands.command()
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RPGCommands(bot))