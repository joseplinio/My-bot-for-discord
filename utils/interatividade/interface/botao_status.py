# Importaçoes:
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
import traceback

class BotaoStatus(discord.ui.View):
    def __init__(self, player):
        super().__init__()
        self._player = player

    @discord.ui.button(label="Status", style=discord.ButtonStyle.green)
    async def mostra_status(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        try:
            if not interaction.response.is_done():
                await interaction.response.defer()
                await interaction.followup.send(
                    embed=criar_embed(
                        titulo=f"``[ Status de {self._player.nome} ]``",
                        descricao=f"Menu para ver suas informações !",
                        color=discord.Color.dark_orange(),
                        campos=[
                            ["Classe:", f"``{self._player.classe}``", True],
                            ["Nível:", f"``{self._player.nivel}``", True],
                            ["Experiência:",f"``{self._player.exp:.2f}/{self._player.calcular_exp_proximo_nivel():.2f}``", True],
                            ["Vida:", f"``{self._player.vida}/{self._player.vida_maxima}``", True],
                            ["Dano:", f"``{self._player.dano}``", True],
                            ["Inventário:", ", ".join(self._player.inventario) if self._player.inventario else "Vazio", False],        
                        ],
                    ),
                    ephemeral=True
                )
            
        except Exception:
            print(traceback.format_exc())