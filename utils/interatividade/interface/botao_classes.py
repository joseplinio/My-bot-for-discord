# Importaçoes:
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed

class BotaoClasses(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Herói", style=discord.ButtonStyle.green)
    async def botao_heroi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if interaction.response.is_done():
            await interaction.followup.send(self.selecionar_classe(interaction, "herói"))
        
    @discord.ui.button(label="Alquimista", style=discord.ButtonStyle.green)
    async def botao_heroi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if interaction.response.is_done():
            await interaction.followup.send(self.selecionar_classe(interaction, "alguimista"))
    
    @discord.ui.button(label="Ranger", style=discord.ButtonStyle.green)
    async def botao_heroi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if interaction.response.is_done():
            await interaction.followup.send(self.selecionar_classe(interaction, "ranger"))

    async def selecionar_classe(self, interaction: discord.Interaction, classe: str):
        if interaction.response.is_done():
            await interaction.followup.send(f"Voce escolheu a classe {classe.capitalize()}")

    async def escolher_classe(self, interaction: discord.Interaction, classe: str) -> str:
        await interaction.followup.send(
            embed=criar_embed(
                descricao=f"Voce escolheu a classe **{classe.capitalize()}**",
                color=discord.Color.dark_green()
            ),
            ephemeral=True
        )
        return classe.capitalize()
    