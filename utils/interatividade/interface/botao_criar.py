# Importaçoes:
import discord
import traceback
from src.cogs.cog_modals import Registro

# Inicio da classe para o botao criar personoagem
class BotaoCriarPerosnagem(discord.ui.View):
    def __init__(self, bot):
            super().__init__()
            self.bot = bot
    
    # Cria o botao configurado e chama a Modal quando clicado 
    @discord.ui.button(label="Criar Personagem!", style=discord.ButtonStyle.green)
    async def botao_criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):        
        try:
            await interaction.response.send_modal(Registro(self.bot)) 
        except Exception:
            print(traceback.format_exc())    
            