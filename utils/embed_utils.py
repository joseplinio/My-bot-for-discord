# Importaçoes:
import discord
from typing import Optional

# Code:
def criar_embed(
    titulo: Optional[str] = None,
    descricao: Optional[str] = None,
    color: discord.Color = discord.Color.default(),
    campos: Optional[list] = None,
    imagem: Optional[str] = None
    ) -> discord.Embed:
    """
    Cria e retorna um embed customizado.
    
    Args:
        title (Optional[str]): O título do embed.
        description (Optional[str]): A descrição principal do embed.
        color (discord.Color): A cor da barra lateral do embed.
        fields (Optional[list]): Uma lista de tuplas contendo (nome, valor, inline).
        imagem (Optional[str]): Um url para a embed.

    Returns:
        discord.Embed: O embed customizado.
    """
    embed = discord.Embed(title=titulo or "", description=descricao or "", color=color)

    if campos:
        for nome, value, inline in campos:
            embed.add_field(name=nome, value=value, inline=inline)

    if imagem:
        embed.set_image(url=imagem)

    return embed