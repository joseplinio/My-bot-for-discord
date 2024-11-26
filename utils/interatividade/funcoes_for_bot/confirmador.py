from utils.interatividade.interface.botao_confirmacao import ConfirmacaoView
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed

async def confirmar_pergunta(interaction: discord.Interaction, escolha: str) -> bool | None:
    """
    Envia uma pergunta para o usuário confirmar sua escolha.

    :param interaction: Objeto da interação do Discord.
    :param escolha: A escolha do usuário a ser confirmada.
    :return: True se o botão "Sim" foi clicado, False se "Não", None se o timeout for atingido.
    """
    # Envia uma mensagem com a classe escolhida e pergunta se quer confirmar
    view_confirmacao = ConfirmacaoView(escolha)
    await interaction.response.send_message(
        embed=criar_embed(
            descricao=f"Você escolheu **{escolha}**. Confirmar?",
            color=discord.Color.dark_green()
        ),
        view=view_confirmacao,
        ephemeral=True
    )
    await view_confirmacao.wait() # Esperar do clique ou o timeout

    return view_confirmacao.confirmacao # O valor retornado