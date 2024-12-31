# Importaçoes:
import discord
import traceback
from typing import List
from src.cogs.fluxodecriacao import FluxoCriacaoPersonagem
from ..funcoes_for_bot.confirmador import confirmar_pergunta
from ..funcoes_for_bot.embed_utils import criar_embed

class BotaoMissoes(discord.ui.View):
    """
    Inicializa a View com os botões baseados nas missoes fornecidas.
    
    :param missoes: Lista de missoes disponíveis.
    :param fluxo: Objeto de fluxo para processar a criação do personagem.
    :param timeout: Tempo limite em segundos para a interação.
    """
    
    def __init__(self, missoes: List[str], fluxo:FluxoCriacaoPersonagem, timeout: int = 30):
        super().__init__(timeout=timeout)

        if not all(isinstance(missao, str) for missao in missoes):
            raise ValueError('Todos os intens dessa lista tem que ser string (str)')
        
        self.missoes = missoes
        self.fluxo = fluxo

        try:
            for missao in missoes:
                self.add_item(self.BotaoMissao(missao, fluxo))
        except Exception:
            print(traceback.format_exc())

    class BotaoMissao(discord.ui.Button, discord.ui.View):
        """
        Botão personalizado para representar uma missao.

        :param missao: Nome da missao.
        :param fluxo: Fluxo para processar a criação do personagem.
        """
        def __init__(self, missao: str, fluxo: FluxoCriacaoPersonagem):
            """
            Botão personalizado para representar uma missao.

            :param missao: Nome da missao.
            :param fluxo: Fluxo para processar a criação do personagem.
            """
            super().__init__(label=missao, style=discord.ButtonStyle.red,custom_id=f"botao_{missao.lower()}")
            self.missao = missao
            self.fluxo = fluxo
                
        async def callback(self, interaction: discord.Interaction):
            """
            Lógica executada quando o botão é clicado.
            """
            try:
                if await confirmar_pergunta(interaction, self.missao):
                    await self.enviar_mensagem_sucesso(interaction, self.missao)
                    await self.fluxo.definir_missao(self, missao=self.missao) # erro nao sei oque pode ser
                    
                else:
                    await self.enviar_tentar_novamente(interaction)
            
            except Exception:
                await interaction.response.send_message(
                    embed=criar_embed(
                        descricao="❌ **Ocorreu um erro ao processar sua escolha. Tente novamente.**",
                        color=discord.Color.dark_red(),
                    ),
                    ephemeral=True
                )
                print(traceback.format_exc())

        async def enviar_mensagem_sucesso(self, interaction: discord.Interaction, missao: str):
            """
            Envia mensagem de sucesso da missao escolhida.
            """
            await interaction.followup.send(
                embed=criar_embed(
                    descricao=f"Ótimo escolha, **{missao}!**",
                    color=discord.Color.dark_green()
                ),
                ephemeral=True,
            )

        async def enviar_tentar_novamente(self, interaction: discord.Interaction):
            """
            Envia mensagem de tentar novamente a escolha de missao.
            """
            await interaction.followup.send(
                embed=criar_embed(
                    descricao="** 📙 Vamos tentar novamente.**",
                    color=discord.Color.dark_orange()
                ),
                ephemeral=True,
                view=BotaoMissoes(
                    missoes=["O Chamado da Lua Rúnica","Os Fragmentos do Nexus Proibido", "O Segredo das Areias do Tempo"],
                    fluxo=FluxoCriacaoPersonagem    
                ),
            )
            