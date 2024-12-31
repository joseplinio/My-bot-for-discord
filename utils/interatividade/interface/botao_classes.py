# Importações
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
import traceback
from utils.interatividade.funcoes_for_bot.confirmador import confirmar_pergunta
from src.cogs.fluxodecriacao import FluxoCriacaoPersonagem
from typing import List
import asyncio
from .botao_misao import BotaoMissoes

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
                    await self.fluxo.definir_classe(self, classe=self.classe)
                else:
                    await self.enviar_tentar_novamente(interaction)

            except Exception as e:
                # Mensagem de erro em caso de falha no processo
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao="❌ **Ocorreu um erro ao processar sua escolha. Tente novamente.**",
                        color=discord.Color.dark_red(),
                    ),
                    ephemeral=True
                )
                print("Erro no callback:", str(e))
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
            await asyncio.sleep(1.3)

            await interaction.followup.send(
                embed=criar_embed(
                    titulo="🌟 Aventura te chama para desafios épicos e mistérios lendários! 🌟\n\n",
                    descricao=(
                        """🌕 Responda ao **chamado** e ``escolha sua missão``! 🌕\n
                        🌑 ``O Chamado da Lua Rúnica``: Encontre os antigos:
                        segredos perdidos sob a luz da lua e desvenda o enigma que conecta reinos esquecidos.\n
                        🔮 ``Os Fragmentos do Nexus Proibido``: Restaure o equilíbrio do multiverso ao recuperar artefatos poderosos que estavam perdidos em dimensões perigosas.\n
                        ⏳ ``O Segredo das Areias do Tempo``: Decifre as mensagens deixadas por viajantes do tempo e evite uma catástrofe que pode apagar a linha temporal.\n"""
                    ),
                    color=discord.Color.dark_red()
                ),
                ephemeral=True,
                view=BotaoMissoes(
                    missoes=["O Chamado da Lua Rúnica","Os Fragmentos do Nexus Proibido", "O Segredo das Areias do Tempo"],
                    fluxo=FluxoCriacaoPersonagem    
                ),
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
                view=BotaoClasses(["Guerreiro", "Alquimista", "Ranger"], self.fluxo)
            )
