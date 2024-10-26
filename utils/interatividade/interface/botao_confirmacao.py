import discord

# Classe para exibir botões de confirmação
class ConfirmacaoView(discord.ui.View):
    def __init__(self, objeto):  # Objeto a ser validado, como nome, etc.
        super().__init__()
        self.objeto = objeto
        self.confirmacao = False
        self.timeout = 30

    @discord.ui.button(label="Sim", style=discord.ButtonStyle.green)
    async def botao_sim(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.confirmacao = True
        await interaction.response.defer()
        self.stop()  # Parar a espera após o clique no botão "Sim"
    
    @discord.ui.button(label="Não", style=discord.ButtonStyle.red)
    async def botao_nao(self, interaction: discord.Interaction, button: discord.ui.Button):  # Renomeado para evitar conflito
        self.confirmacao = False
        await interaction.response.defer()
        self.stop()  # Parar a espera após o clique no botão "Não"
