# Importaçoes:
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
import discord
import re
import traceback
from utils.interatividade.interface.botao_classes import BotaoClasses

class Registro(discord.ui.Modal):
    def __init__(self, bot):
        super().__init__(title="Registrar Nome do Personagem")
        self.bot = bot

        # Campo para o nome
        self.nome = discord.ui.TextInput(
            label="Digite o nome do seu personagem",
            placeholder="Exemplo: Hapz",
            max_length=10,
        )
        self.add_item(self.nome)  # Adiciona o TextInput à Modal

    async def on_submit(self, interaction: discord.Interaction):
        from utils.interatividade.interface.botao_criar import BotaoCriarPerosnagem
        nome = self.nome.value.strip()

        # Limpeza do nome: substitui espaços por sublinhados e remove caracteres '<' e '>'
        nome_limpo = re.sub(r'\s+', '_', nome)
        nome_limpo = re.sub(r'[<>]', '', nome_limpo)

        # Validação do nome
        if not re.match("^[A-Za-z0-9_-]*$", nome_limpo):
            # Envia uma mensagem de erro se o nome não for válido
            await interaction.response.send_message(
                embed=criar_embed(
                    descricao="** ❌ Nome inválido! Use apenas letras, números, hífens e sublinhados.**",
                    color=discord.Color.dark_red(),
                ),
                ephemeral=True
            )
            return

        # Pergunta de confirmação do nome
        try:
            if await self.confirmar_pergunta(interaction, nome_limpo):
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao=f"Ótimo nome, **{nome_limpo}!**",
                        color=discord.Color.dark_green()
                    ),
                    ephemeral=True,
                )
                classes = BotaoClasses()
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao="🌌 **Prepare-se para uma jornada épica repleta de desafios e conquistas!** 🌌\n\n"
                            "🛡️ **Escolha sua classe e defina seu destino!** Use os `botes` para selecionar entre valentes guerreiros, "
                            "astutos Alquimistas e ágeis Rangers. Cada classe traz habilidades únicas que irão moldar sua jornada.\n\n"
                            "⚔️ **Crie seu personagem e prepare-se para enfrentar inimigos poderosos, explorar reinos fascinantes e descobrir tesouros inimagináveis!**\n\n"
                            "🌠 **Que a sorte e a bravura estejam sempre ao seu lado!** 🍀✨",
                        color=discord.Color.dark_green()
                    ),
                    ephemeral=True,
                    view=classes
                )

            else:
                # Instancia o botao para ser enviado:
                view = BotaoCriarPerosnagem(self.bot)
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao="** 📙 Vamos tentar novamente.**",
                        color=discord.Color.dark_orange()
                    ),
                    ephemeral=True,
                    view=view
                )

        except Exception:
            print(traceback.format_exc())
            
    async def confirmar_pergunta(self, interaction: discord.Interaction, objeto) -> bool:
        # Cria uma view para confirmação
        view = ConfirmacaoView(objeto)
        await interaction.response.send_message(
            embed=criar_embed(
                descricao=f"Você escolheu o nome **{objeto}**. Confirmar?",
                color=discord.Color.dark_green()
            ),
            view=view,
            ephemeral=True
        )
        await view.wait()
        return view.confirmacao
