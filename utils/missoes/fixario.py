# Importaçoes
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed

class ChamdoDaLua(): # inicio da classe
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def chamdo_da_lua(self) -> discord.Embed:
        return criar_embed( # Mensagem da misao
            titulo="O Chamado da Lua Rúnica 🌑",
            descricao="🌕 Atenda ao chamado da lua de sangue e mergulhe em uma jornada mística!\n\n"
                "🔮 Explore terras sombrias e descubra segredos enterrados sob o brilho da lua rúnica. Somente os mais corajosos poderão desvendar a verdade por trás deste antigo presságio.\n\n"
                "🗡️ Prepare-se para enfrentar criaturas sombrias e desvendar enigmas ancestrais. Que a lua guie seus passos nesta aventura repleta de magia e mistério!",
            color=discord.Color.dark_red(),
            imagem="https://i.pinimg.com/736x/62/f9/3b/62f93bbf77742d6154e770cef98cce5a.jpg"
        )

class FragmentosNexos():
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def fragmentos_nexos(self) -> discord.Embed:
        return criar_embed( # Mensagem da misao
            titulo="Os Fragmentos do Nexus Proibido 🔮",
            descricao="💠 Descubra o poder oculto dos fragmentos proibidos e desafie o destino!\n\n"
                "🌀 Viaje pelas terras corrompidas em busca de peças perdidas de um poder inimaginável. Cada fragmento esconde um segredo, e cabe a você revelar o que está além do véu do proibido.\n\n"
                "⚔️ Enfrente inimigos poderosos e perigos desconhecidos. Apenas os mais destemidos sobreviverão para juntar todos os fragmentos e desvendar o mistério do Nexus!",
            color=discord.Color.dark_purple(),
            imagem="https://i.pinimg.com/736x/4c/9f/af/4c9faf54c98ebc2b6475b38e8223e47c.jpg"
        )

class AreiasDoTempo():
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def areias_tempo(self) -> discord.Embed:
        return criar_embed( # Mensagem da misao
            titulo="O Segredo das Areias do Tempo ⏳",
            descricao="🏜️ Aventure-se nas profundezas das dunas eternas e revele segredos do passado!\n\n"
                "⌛ O tempo é uma ilusão nas areias douradas. Encontre pistas escondidas e desvende profecias antigas enterradas pelo vento.\n\n"
                "🛡️ Prepare-se para enfrentar desafios ancestrais e criaturas esquecidas. Apenas aqueles que dominarem o fluxo do tempo sairão vitoriosos e descobrirão o que está escondido nas areias!",
            color=discord.Color.dark_orange(),
            imagem="https://i.pinimg.com/736x/92/14/51/9214513342871c67ba9a3b210c55d53b.jpg"
        )
