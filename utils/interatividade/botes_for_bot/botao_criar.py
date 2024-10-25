# Importaçoes:
import discord
from src.cogs.commands_rpg import RPGCommands
import traceback

# Inicio da classe para o botao criar personoagem
class BotaoCriarPerosnagem(discord.ui.View):
    def __init__(self, bot):
            super().__init__()
            self.bot = bot
    
    try:
        # Cria o botao configurado, fazendo o metodo callback quando o botao e clicado 
        # despareando a funçao, logo depois chama a funçao criar personagem: 
        @discord.ui.button(label="Criar Personagem!", style=discord.ButtonStyle.green)
        async def botao_criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):
            comando_criar = RPGCommands(self.bot)
            await interaction.response.send_message(await comando_criar.criar_personagem(interaction), ephemeral= True)
            
    except Exception:
        print(traceback.format_exc())    
        
        

