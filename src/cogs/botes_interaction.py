import discord
from discord.ui import View
import traceback
from utils.embed_utils import criar_embed

# Classe para gerar os botões
class BotesForRpg(View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.players = {}  # Adicione a lista de jogadores aqui

    @discord.ui.button(label="Criar Personagem!", style=discord.ButtonStyle.success)
    async def botao_criar_personagem(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            # Verifique se o usuário já tem um personagem
            if interaction.user.id in self.players:
                await interaction.response.send_message("**Você já tem um personagem. Use ``!status`` para ver suas informações.**", ephemeral=True)
                return

            # Instanciando a lógica de criação de personagem
            criando_personagem = interaction.client.cogs["RPGCommands"].MetosCriarPersonagem(self.bot)

            # Pergunta o nome e a classe
            nome = await criando_personagem.pergunta_nome(interaction)
            if not nome:
                await interaction.response.send_message("**Criação de personagem cancelada.**", ephemeral=True)
                return

            classe = await criando_personagem.pergunta_classe(interaction)
            if not classe:
                await interaction.response.send_message("**Criação de personagem cancelada.**", ephemeral=True)
                return

            # Criando o personagem
            player = interaction.client.cogs["RPGCommands"].Player(nome, 1, 100, 20, {}, 0, classe)
            self.players[interaction.user.id] = player
            await interaction.response.send_message(embed=criar_embed(
                descricao=f"Personagem ``{player.nome}``, classe ``{player.classe}`` foi criado com sucesso!",
                color=discord.Color.dark_green(),
                campos=[
                    ["**[Dica]**", "*Clique* no botão ``status`` *para ver suas informações.*", True]
                ]
            ), ephemeral=True)

        except Exception:
            print(traceback.format_exc())
