import discord
import traceback
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_classes import BotaoClasses  # Importa o BotaoClasses separadamente
from .fluxodecriacao import FluxoCriacaoPersonagem
from utils.interatividade.funcoes_for_bot.confirmador import confirmar_pergunta
import asyncio

class ModalNome(discord.ui.Modal):
    """
    Modal para definir o nome do personagem. Interage diretamente com o fluxo de criação.
    """
    def __init__(self, bot, fluxo: FluxoCriacaoPersonagem):
        super().__init__(title="Registrar Nome do Personagem")
        self.bot = bot
        self.fluxo = fluxo

        # Campo para o nome do personagem
        self.nome = discord.ui.TextInput(
            label="Digite o nome do seu personagem",
            placeholder="Exemplo: Hapz",
            max_length=10,  # Limite máximo de caracteres
        )
        self.add_item(self.nome)

    async def on_submit(self, interaction: discord.Interaction):
        """
        Trata o evento de submissão do modal, incluindo validação e confirmação do nome.
        """
        try:
            nome_input = self.nome.value
            if not isinstance(nome_input, str) or nome_input.strip() == "":
                await interaction.response.send_message(
                    embed=criar_embed(
                        descricao="** ❌ Nome inválido! O nome precisa ser uma string com caracteres válidos.**",
                        color=discord.Color.dark_red(),
                    ),
                    ephemeral=True
                )
                return
        
            if nome_input:
                # Confirmação do nome
                resposta = await confirmar_pergunta(interaction, nome_input)
                
                if resposta is True:
                    await self.enviar_mensagem_sucesso(interaction, nome_input)
                    self.fluxo.definir_nome(nome_input)

                elif resposta is False:
                    await self.enviar_tentar_novamente(interaction)

            else:
                await self.enviar_nome_invalido(interaction)

        except Exception:
            print(traceback.format_exc())

    async def enviar_mensagem_sucesso(self, interaction: discord.Interaction, nome: str):
        """
        Envia mensagem confirmando o nome e exibindo as opções de classes.
        """
        await interaction.followup.send(
            embed=criar_embed(
                descricao=f"Ótimo nome, **{nome}!**",
                color=discord.Color.dark_green()
            ),
            ephemeral=True,
        )
        await asyncio.sleep(1.3)

        await interaction.followup.send(
            embed=criar_embed(
                descricao=(
                    "🌌 **Prepare-se para uma jornada épica repleta de desafios e conquistas!** 🌌\n\n"
                    "🛡️ **Escolha sua classe e defina seu destino!** Selecione entre valentes Guerreiros, "
                    "astutos Alquimistas e ágeis Rangers. Cada classe traz habilidades únicas que irão moldar sua jornada.\n\n"
                    "⚔️ **Crie seu personagem e prepare-se para enfrentar inimigos poderosos, explorar reinos fascinantes e descobrir tesouros inimagináveis!**\n\n"
                    "🌠 **Que a sorte e a bravura estejam sempre ao seu lado!** 🍀✨"
                ),
                color=discord.Color.dark_green()
            ),
            ephemeral=True,
            view=BotaoClasses(["Guerreiro", "Ranger", "Alquimista"], FluxoCriacaoPersonagem) # Exibe a tela para escolher a classe
        )

    async def enviar_nome_invalido(self, interaction: discord.Interaction):
        """
        Envia mensagem indicando que o nome fornecido é inválido.
        """
        await interaction.response.send_message(
            embed=criar_embed(
                descricao="** ❌ Nome inválido! Use apenas letras, números, hífens e sublinhados.**",
                color=discord.Color.dark_red(),
            ),
            ephemeral=True
        )
    
    async def enviar_tentar_novamente(self, interaction: discord.Interaction):
        """
        Envia mensagem pedindo para tentar novamente.
        """
        from utils.interatividade.interface.botao_start import BotaoCriarPersonagem

        await interaction.followup.send(
            embed=criar_embed(
                descricao="** 📙 Vamos tentar novamente.**",
                color=discord.Color.dark_orange()
            ),
            ephemeral=True,
            view=BotaoCriarPersonagem(self.bot)
        )
