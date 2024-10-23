# Impotaçoes:
from utils.interatividade.embeds.embed_utils import criar_embed
import discord
import traceback

# Funçao para iniciar o bot com mensage para o user:
async def iniciar(channel):
        """Usado para inicar o jogo"""
        try:

            await channel.send(embed=criar_embed(
                color=discord.Color.dark_green(),
                    
                )
            )
            
            await channel.send(embed=criar_embed(
                titulo="🌟 **Bem-vindo(a) ao Mundo de Aventuras!** 🌟\n\n",
                color=discord.Color.dark_green(),
                descricao="Prepare-se para embarcar em uma jornada épica de batalhas, descobertas e evolu'ção! ⚔️🛡️\n"
                    "Crie seu personagem, usando `Criar Personagem`!\n\n"
                    "Que as estrelas guiem o seu caminho, e a sorte esteja sempre ao seu lado! 🍀✨\n\n",
                ),
            )

        except Exception:
            print(traceback.format_exc())