# Importações
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView

class BotaoClasses(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Guerreiro", style=discord.ButtonStyle.green)
    async def botao_guerreiro(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.escolher_classe(interaction, "Guerreiro")

    @discord.ui.button(label="Alquimista", style=discord.ButtonStyle.green)
    async def botao_alquimista(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.escolher_classe(interaction, "Alquimista")

    @discord.ui.button(label="Ranger", style=discord.ButtonStyle.green)
    async def botao_ranger(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.escolher_classe(interaction, "Ranger")

    async def escolher_classe(self, interaction: discord.Interaction, classe: str):
        # Envia uma mensagem com a classe escolhida e pergunta se quer confirmar
        view_confirmacao = ConfirmacaoView(classe)
        await interaction.response.send_message(
            embed=criar_embed(
                descricao=f"Você escolheu a classe **{classe}**. Confirmar?",
                color=discord.Color.dark_green()
            ),
            view=view_confirmacao,
            ephemeral=True
        )
        await view_confirmacao.wait()

        # Valida a escolha da classe com base na resposta do usuário
        if view_confirmacao.confirmacao:
            await interaction.followup.send(
                embed=criar_embed(
                    descricao=f"Você confirmou a classe **{classe}**! Prepare-se para sua jornada!",
                    color=discord.Color.dark_green()
                ),
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                embed=criar_embed(
                    descricao="**📙 Escolha sua classe novamente.**",
                    color=discord.Color.dark_orange()
                ),
                ephemeral=True,
            )
