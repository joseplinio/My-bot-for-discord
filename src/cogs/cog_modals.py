# Importaçoes:
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
import discord
import re
import traceback

class Registro(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Registrar Nome do Personagem")

        # Campo para o nome
        self.nome = discord.ui.TextInput(
            label="Digite o nome do seu personagem",
            placeholder="Exemplo: Hapz",
            max_length=10,
        )
        self.add_item(self.nome)  # Adiciona o TextInput à Modal

    async def on_submit(self, interaction: discord.Interaction):
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
                    ephemeral=True
                )
            else:
                await interaction.followup.send(
                    embed=criar_embed(
                        descricao="** ✴️ Vamos tentar novamente.**",
                        color=discord.Color.dark_orange()
                    ),
                    ephemeral=True
                )
        except Exception:
            print(traceback.format_exc())
            
    async def confirmar_pergunta(self, interaction, objeto):
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
