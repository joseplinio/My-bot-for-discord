# Importações
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
import traceback
from utils.interatividade.funcoes_for_bot.confirmador import confirmar_pergunta
from src.cogs.fluxodecriacao import FluxoCriacaoPersonagem
from typing import List

class BotaoClasses(discord.ui.View):
    def __init__(self, classes: List[str], fluxo: FluxoCriacaoPersonagem, timeout: int = 30):
        """
        Inicializa a View com os botões baseados nas classes fornecidas.
        
        :param classes: Lista de classes disponíveis.
        :param fluxo: Objeto de fluxo para processar a criação do personagem.
        :param timeout: Tempo limite em segundos para a interação.
        """
        # Validação da lista de classes
        if not all(isinstance(classe, str) for classe in classes):
            raise ValueError("A lista de classes deve conter apenas strings.")
        
        super().__init__(timeout=timeout)
        self.classes = classes
        self.fluxo = fluxo

        # Criar botões dinamicamente
        try:
            for classe in classes:
                self.add_item(self.BotaoClasse(classe, fluxo))
        except Exception:
            print(traceback.format_exc())

    class BotaoClasse(discord.ui.Button):
        def __init__(self, classe: str, fluxo: FluxoCriacaoPersonagem):
            """
            Botão personalizado para representar uma classe.

            :param classe: Nome da classe.
            :param fluxo: Fluxo para processar a criação do personagem.
            """
            super().__init__(label=classe, style=discord.ButtonStyle.green, custom_id=f"botao_{classe.lower()}")
            self.classe = classe
            self.fluxo = fluxo
        
        async def callback(self, interaction: discord.Interaction):
            """
            Lógica executada quando o botão é clicado.
            """
            try:
                if await confirmar_pergunta(interaction, self.classe):
                    await self.enviar_mensagem_sucesso(interaction, self.classe)
                    await self.fluxo.definir_classe(self.classe)

                else:
                    await self.enviar_tentar_novamente()

            except Exception:
                await interaction.response.send_message(
                    embed=criar_embed(
                        descricao="❌ **Ocorreu um erro ao processar sua escolha. Tente novamente.**",
                        color=discord.Color.dark_red(),
                    ),
                    ephemeral=True
                )
                print(traceback.format_exc())

        async def enviar_mensagem_sucesso(self, interaction: discord.Interaction, classe: str):
            """
            Envia mensagem de sucesso da classe escolhida.
            """
            await interaction.followup.send(
                embed=criar_embed(
                    descricao=f"Ótimo escolha, **{classe}!**",
                    color=discord.Color.dark_green()
                ),
                ephemeral=True,
            )
        
        async def enviar_tentar_novamente(self, interaction: discord.Interaction):
            """
            Envia mensagem de tentar novamente a escolha de classe.
            """
            await interaction.followup.send(
                embed=criar_embed(
                    descricao="** 📙 Vamos tentar novamente.**",
                    color=discord.Color.dark_orange()
                ),
                ephemeral=True,
                view=BotaoClasses(["Guerreiro", "Alquimista", "Ranger"])
            )
