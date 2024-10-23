# Impotaçoes:
from utils.interatividade.embeds.embed_utils import criar_embed
import discord
import traceback
from utils.interatividade.botes.criar_personagem import BotaoCriarPerosnagem

# Funçao para iniciar o bot com mensage para o user:
async def iniciar(ctx):
        """Usado para inicar o jogo"""
        try:

            await ctx.send(embed=criar_embed(
                imagem="https://i.pinimg.com/originals/d8/bf/32/d8bf3287a8ad85cc5270b26be1e11e4b.gif",
                color=discord.Color.dark_green()
                )
            )
            
            iniciar_jogo = await ctx.send(embed=criar_embed(
                titulo="🌟 **Bem-vindo(a) ao Mundo de Aventuras!** 🌟\n\n",
                color=discord.Color.dark_green(),
                descricao="Prepare-se para embarcar em uma jornada épica de batalhas, descobertas e evolu'ção! ⚔️🛡️\n"
                    "Crie seu personagem, usando `Criar Personagem`!\n\n"
                    "Que as estrelas guiem o seu caminho, e a sorte esteja sempre ao seu lado! 🍀✨\n\n",
                ),
            )
            view = BotaoCriarPerosnagem()
            await iniciar_jogo.edit(view=view)
            await view.wait()

        except Exception:
            print(traceback.format_exc())