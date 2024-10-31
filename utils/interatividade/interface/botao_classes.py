# Importaçoes:
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed

class BotaoClasses(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Guerreiro", style=discord.ButtonStyle.green)
    async def botao_guerreiro(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.response.is_done():
            await interaction.response.defer()
        await interaction.followup.send(await self.escolher_classe(interaction, "guerreiros"))
    
    @discord.ui.button(label="Alquimista", style=discord.ButtonStyle.green)
    async def botao_alquimista(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.response.is_done():
            await interaction.response.defer()
        await interaction.followup.send(await self.escolher_classe(interaction, "alquimista"))
    
    @discord.ui.button(label="Ranger", style=discord.ButtonStyle.green)
    async def botao_ranger(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.response.is_done():
            await interaction.response.defer()
        await interaction.followup.send(await self.escolher_classe(interaction, "ranger"))

    async def escolher_classe(self, interaction: discord.Interaction, classe: str) -> str:
        await interaction.followup.send(
            embed=criar_embed(
                descricao=f"Voce escolheu a classe **{classe.capitalize()}**",
                color=discord.Color.dark_green()
            ),
            ephemeral=True
        )
        return classe.capitalize()
    