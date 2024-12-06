# Importaçoes:
import discord
from utils.missoes.fixario import ChamdoDaLua, FragmentosNexos, AreiasDoTempo
import traceback
from typing import List
from src.cogs.fluxodecriacao import FluxoCriacaoPersonagem
from ..funcoes_for_bot.confirmador import confirmar_pergunta

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

    class BotaoMissao(discord.ui.Button):
        """
        Botão personalizado para representar uma missao.

        :param missao: Nome da classe.
        :param fluxo: Fluxo para processar a criação do personagem.
        """
        def __init__(self, missao: str, fluxo: FluxoCriacaoPersonagem):
            super().__init__(label=missao, style=discord.ButtonStyle.red, custom_id=f"botao_{missao.lower()}")
            self.missao = missao
            self.fluxo = fluxo
                
        async def callback(self, interaction: discord.Interaction):
            """
            Lógica executada quando o botão é clicado.
            """
            try:
                await confirmar_pergunta(interaction, self.missao)
                
            except Exception:
                print(traceback.format_exc())




    # # Botes para as missoes O Chamado da Lua Rúnica, Os Fragmentos do Nexus Proibido, O Segredo das Areias do Tempo
    # @discord.ui.button(label="O Chamado da Lua Rúnica", style=discord.ButtonStyle.danger)
    # async def botao_chamado_lua(self, interaction: discord.Interaction, bottun: discord.ui.Button):
    #     try:
    #         await interaction.response.defer() # Metodo de espera de resposta
    #         await interaction.followup.send(embed= await ChamdoDaLua(interaction).chamdo_da_lua(), ephemeral=True)
    #         self.stop()
    #     except Exception:
    #         print(traceback.format_exc())
            
    # @discord.ui.button(label="Os Fragmentos do Nexus Proibido", style=discord.ButtonStyle.danger)
    # async def botao_frang_nexos(self, interaction: discord.Interaction, bottun: discord.ui.Button):
    #     try:
    #         await interaction.response.defer() # Metodo de espera de resposta
    #         await interaction.followup.send(embed= await FragmentosNexos(interaction).fragmentos_nexos(), ephemeral=True)
    #         self.stop()
    #     except Exception:
    #         print(traceback.format_exc())
            
    # @discord.ui.button(label="O Segredo das Areias do Tempo", style=discord.ButtonStyle.danger)
    # async def botao_areias_tempo(self, interaction: discord.Interaction, bottun: discord.ui.Button):
    #     try:
    #         await interaction.response.defer() # Metodo de espera de resposta
    #         await interaction.followup.send(embed= await AreiasDoTempo(interaction).areias_tempo(), ephemeral=True)
    #         self.stop()
    #     except Exception:
    #         print(traceback.format_exc())
            