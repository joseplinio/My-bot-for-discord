# importaçoes:
import discord
import traceback
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed

class BotaoJogar(discord.ui.View):
    def __init__(self):
        super().__init__()

    # Botao jogar
    @discord.ui.button(label="Jogar", style=discord.ButtonStyle.green)
    async def botao_jogar(self, interaction: discord.Interaction, button: discord.ui.Button) -> discord.Embed:
        await interaction.response.defer()
        #await interaction.followup.send()
        pass
            
