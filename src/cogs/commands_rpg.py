# Importaçoes:
from discord.ext import commands
import discord
from src.models.inimigo import Inimigo
from src.models.player import Player
from utils.interatividade.embeds import criar_embed
import asyncio
import traceback
import random
from discord.ui import View, Button

# Classe dos comandos para o RPG:
class RPGCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.players = {}
        self.batalhas_ativas = {}

    async def status(self, ctx):
        """Mostra o status do personagem do usuário."""
        try:
        
            player = self.players.get(ctx.author.id)
            if not player:
                await ctx.send("*Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.*")
                return
            
            await ctx.send(embed=criar_embed(
            titulo=f"``[ Status de {player.nome} ]``",
                descricao=f"Menu para ver suas informações !",
                color=discord.Color.purple(),
                campos=[
                    ["Classe:", f"``{player.classe}``", True],
                    ["Nível:", f"``{player.nivel}``", True],
                    ["Experiência:",f"``{player.exp:.2f}/{player.calcular_exp_proximo_nivel():.2f}``", True],
                    ["Vida:", f"``{player.vida}/{player.vida_maxima}``", True],
                    ["Dano:", f"``{player.dano}``", True],
                    ["Inventário:", ", ".join(player.inventario) if player.inventario else "Vazio", False],        
                ]
            ))
            
        except Exception:
            print(traceback.format_exc())

    async def lutar(self, ctx):
        """Inicia uma luta contra um inimigo aleatório."""
        try:

            player = self.players.get(ctx.author.id)

            if not player:
                await ctx.send("*Você ainda não tem um personagem. Use ``!criar_personagem`` para criar um.*")
                return
            
            if ctx.author.id in self.batalhas_ativas:
                await ctx.send("*Você já está em uma batalha!*")
                return
            
            inimigo = Inimigo("Dragão", 100, 1, 15, 100)
            inimigo.adicionar_jogador_ao_combate(player)
            self.batalhas_ativas[ctx.author.id] = inimigo

            await ctx.send(embed=criar_embed(
                titulo="Batalha Iniciada!",
                descricao=f"Você encontrou o(a) {inimigo.nome}\n{inimigo.descricao}",
                color=discord.Color.purple(),
                imagem="https://i.pinimg.com/originals/21/fc/37/21fc376f984e1af95f3e748efe07ecd4.gif",
                campos=[
                    ["**Você [ V.d | N.v ]**:", f"``{player.vida}/{player.vida_maxima}`` | ``{player.nivel}``", True],
                    ["**Inimigo [ V.d | N.v ]**:", f"``{inimigo.vida}/{inimigo.vida_maxima}`` | ``{inimigo.nivel}``", True],
                    ["**[ Comando ]**", "Use ``!atacar`` para atacar o inimigo ou ``!fugir`` para tentar escapar.", False]
                ]
            ))

        except Exception:
            print(traceback.format_exc())
            
    async def atacar(self, ctx):
        """Usado para atacar o inimigo durante uma batalha"""
        try: 

            player = self.players.get(ctx.author.id)
            inimigo = self.batalhas_ativas.get(ctx.author.id)

            if not player or not inimigo:
                await ctx.send("*Você não está em uma batalha!*")
                return
            
            await asyncio.sleep(1)
            player.atacar_inimigo(inimigo)
            await ctx.send(embed=criar_embed(
                titulo="``[ Seu Turno ]``",
                color=discord.Color.blue(),
                imagem="https://i.pinimg.com/originals/48/d2/d4/48d2d446903509f10103848b5fe648b9.gif",
                campos=[
                    ["", f"Você atacou o **{inimigo.nome}** e causou **{player.dano} de dano!**", False],
                    ["Vida do inimigo: ",f"``{inimigo.vida}/{inimigo.vida_maxima}``", True]
                ]
            ))
            
            if inimigo.vida <= 0:
    
                exp, recompensas = inimigo.morrer()
                player.ganhar_exp(exp)
               
                for item in recompensas:
                    player.add_item(item)
                
                await asyncio.sleep(1)
                await ctx.send(embed=criar_embed(
                    titulo="``[ Vitória! ]``",
                    descricao=f"Você derrotou o {inimigo.nome} **!** \n depois de sua morte ele deixou cair:",
                    color=discord.Color.green(),
                    campos=[
                        ["*Recompensas:*", f"*Exp:* {inimigo.exp}\n *Items:* {", ".join(recompensas)}", False]
                    ],
                    imagem=""
                ))

                del self.batalhas_ativas[ctx.author.id]

            else:

                await asyncio.sleep(2)
                nome_inimigo, dano_inimigo = inimigo.atacar_jogador(player)
                await ctx.send(embed=criar_embed(
                    titulo="``[ Turno do Inimigo ]``",
                    color=discord.Color.red(),
                    imagem="https://i.pinimg.com/originals/0b/2f/26/0b2f260d15a6ff832c1f6e1e40374155.gif",
                    campos=[
                        ["", f"O **{nome_inimigo}** atacou você e causou **{dano_inimigo} de dano!**", False],
                        ["Sua Vida: ", f"``{player.vida}/{player.vida_maxima}``", False]
                    ]
                ))

                await asyncio.sleep(2)
                await ctx.send(embed=criar_embed(
                    titulo="``[ Resultado da Batalha ]``",
                    descricao=f"Uma batalha acirrada entre ``{player.nome}`` e ``{inimigo.nome}``\n **Resulta:**",
                    color=discord.Color.green(),   
                    campos=[
                        ["*Sua Vida*", f"``{player.vida}/{player.vida_maxima}``", True],
                        ["*Vida do Inimigo*", f"``{inimigo.vida}/{inimigo.vida_maxima}``", True]
                    ]
                ))

                if player.vida <= 0:

                    await ctx.send(embed=criar_embed(
                        titulo="``[ Derrota! ]``",
                        descricao=f"Você foi derrotada pelo ``{inimigo.nome}``\n nao fique mal, *você sempre pode tentar de novo !*",
                        color= discord.Color.red(),
                    ))
                        
                    del self.batalhas_ativas[ctx.author.id]    
        
        except Exception:
            print(traceback.format_exc())

    async def fugir(self, ctx) -> None:
        """Usado para fugir de um combate"""
        try:

            player = self.players.get(ctx.author.id)
            inimigo = self.batalhas_ativas.get(ctx.author.id)

            if not ctx.author.id in self.batalhas_ativas:
                await ctx.send("**Você não está em uma batalha!**")
                return

            if random.random() < 0.50:

                await asyncio.sleep(1)
                del self.batalhas_ativas[ctx.author.id]
                await ctx.send(embed=criar_embed(
                    titulo="``[ Seu Turno ]``",
                    color=discord.Color.blue(),
                    campos=[
                        ["", f"**Você conseguiu fugir com sucesso!**  do **{inimigo.nome}**", False]
                    ]
                ))
                
            else:

                await asyncio.sleep(1)
                await ctx.send(embed=criar_embed(
                    titulo="``[ Seu Turno ]``",
                    color=discord.Color.blue(),
                    campos=[
                        ["", f"Você tenta fogir, mas **falhou!** ", False],
                    ]
                ))

                await asyncio.sleep(1)
                inimigo = self.batalhas_ativas.get(ctx.author.id)
                nome_inimigo, dano_inimigo = inimigo.atacar_jogador(player)
                await ctx.send(embed=criar_embed(
                    titulo="``[ Turno do Inimigo ]``",
                    color=discord.Color.red(),
                    imagem="https://i.pinimg.com/originals/0b/2f/26/0b2f260d15a6ff832c1f6e1e40374155.gif",
                    campos=[
                        ["", f"O **{nome_inimigo}** atacou você e causou **{dano_inimigo} de dano!**", False],
                        ["Sua Vida: ", f"``{player.vida}/{player.vida_maxima}``", False]
                    ]
                ))
                
                if player.vida <= 0:
                    await asyncio.sleep(1)
                    await ctx.send(embed=criar_embed(
                        titulo="``[ Derrota! ]``",
                        descricao=f"Você foi derrotada pelo ``{inimigo.nome}``\n nao fique mal, *você sempre pode tentar de novo !*",
                        color= discord.Color.red(),
                    ))
                        
                    del self.batalhas_ativas[ctx.author.id]

        except Exception:
            print(traceback.format_exc())
       
async def setup(bot):
    await bot.add_cog(RPGCommands(bot))
    