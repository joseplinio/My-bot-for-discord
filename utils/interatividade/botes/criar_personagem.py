# Importaçoes:
import discord
from utils.interatividade.embeds.embed_utils import criar_embed

# Inicio da classe para o botao criar personoagem
class BotaoCriarPerosnagem(discord.ui.View):
    def __init__(self):
            super().__init__()

    @discord.ui.button(label="Criar Personagem!", style=discord.ButtonStyle.green)
    async def botao_criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(embed=criar_embed(
            titulo="Parabens",
            descricao="voce e broxa"
            
            )
        )
        

