# Importaçoes:
import discord
import traceback
from src.cogs.modal_nome import ModalNome
from src.cogs.fluxodecriacao import FluxoCriacaoPersonagem

# Início da classe para o botão criar personagem
class BotaoCriarPersonagem(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    # Cria o botão configurado e chama a Modal quando clicado
    @discord.ui.button(label="Criar Personagem!", style=discord.ButtonStyle.green)
    async def botao_criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):        
        try:
            fluxo = FluxoCriacaoPersonagem() # Inicializando a classe `FluxoCriacaoPersonagem`
            # Passando os parâmetros necessários para `ModalNome`
            await interaction.response.send_modal(ModalNome(self.bot, fluxo))
            self.stop()
        except Exception:
            print(traceback.format_exc())
