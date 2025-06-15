# Impotaçoes:
from utils.funcoes_for_bot.embed_utils import criar_embed
from discord.ext import commands
import traceback
import discord
from utils.interatividade.interface.auxilio_botes.botao_start import BotaoCriarPersonagem

# Funçao para iniciar o bot com mensage para o user:
async def iniciar(ctx: commands.Context, bot):
    """Usado para inicar o jogo, no casso a mensagem do inicio do jogo"""
    try:
        iniciar_jogo = await ctx.send(
            embed=criar_embed(
                titulo="🌟 **Bem-vindo(a) ao Mundo de Aventuras!** 🌟\n\n",
                descricao="Prepare-se para embarcar em uma jornada épica de batalhas, descobertas e evolu'ção! ⚔️🛡️\n"
                    "Começe sua jornada usando `Start`!\n\n"
                    "Que as estrelas guiem o seu caminho, e a sorte esteja sempre ao seu lado! 🍀✨\n\n",
                color=discord.Color.dark_green(),     
            ),
        )

        # Instancia o o botao para ser envida:
        view = BotaoCriarPersonagem(bot)
        await iniciar_jogo.edit(view=view)
        await view.wait()
        
    except Exception:
        print(traceback.format_exc())