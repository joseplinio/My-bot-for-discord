# Importações
import discord
import re
import traceback
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
from utils.interatividade.interface.botao_classes import BotaoClasses  # Importa o BotaoClasses separadamente

class Registro(discord.ui.Modal):
    def __init__(self, bot):
        super().__init__(title="Registrar Nome do Personagem")
        self.bot = bot

        # Campo para o nome do personagem
        self.nome = discord.ui.TextInput(
            label="Digite o nome do seu personagem",
            placeholder="Exemplo: Hapz",
            max_length=10,
        )
        self.add_item(self.nome)

    async def on_submit(self, interaction: discord.Interaction):
        from utils.interatividade.interface.botao_criar import BotaoCriarPerosnagem

        nome = self.nome.value.strip()

        # Limpeza e validação do nome
        nome_limpo = re.sub(r'\s+', '_', nome)
        nome_limpo = re.sub(r'[<>]', '', nome_limpo)

        if not re.match("^[A-Za-z0-9_-]*$", nome_limpo):
            await interaction.response.send_message(
                embed=criar_embed(
                    descricao="** ❌ Nome inválido! Use apenas letras, números, hífens e sublinhados.**",
                    color=discord.Color.dark_red(),
                ),
                ephemeral=True
            )
            return

        # Confirmação do nome
        try:
            if await self.confirmar_pergunta(interaction, nome_limpo):
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao=f"Ótimo nome, **{nome_limpo}!**",
                        color=discord.Color.dark_green()
                    ),
                    ephemeral=True,
                )

                # Exibe a tela para escolher a classe
                view_classe = BotaoClasses()  # Instancia a classe BotaoClasses
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
                    view=view_classe
                )
            else:
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao="** 📙 Vamos tentar novamente.**",
                        color=discord.Color.dark_orange()
                    ),
                    ephemeral=True,
                    view=BotaoCriarPerosnagem(self.bot)
                )
        except Exception:
            print(traceback.format_exc())

    async def confirmar_pergunta(self, interaction: discord.Interaction, escolha: str) -> bool:
        # Cria uma view para confirmação
        view = ConfirmacaoView(escolha)
        await interaction.response.send_message(
            embed=criar_embed(
                descricao=f"Você escolheu **{escolha}**. Confirmar?",
                color=discord.Color.dark_green()
            ),
            view=view,
            ephemeral=True
        )
        await view.wait()
        return view.confirmacao
