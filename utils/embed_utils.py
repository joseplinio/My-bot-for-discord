# Importaçoes:
import discord
from typing import Optional

# Code:
async def criar_embed(
    titulo: Optional[str] = None,
    descriçao: Optional[str] = None,
    color: discord.Color = discord.Color.default(),
    campos: Optional[list] = None
    ) -> discord.Embed:
    """Cria e retorna um embed customizado.
    
    Args:
        title (Optional[str]): O título do embed.
        description (Optional[str]): A descrição principal do embed.
        color (discord.Color): A cor da barra lateral do embed.
        fields (Optional[list]): Uma lista de tuplas contendo (nome, valor, inline).

    Returns:
        discord.Embed: O embed customizado.
    """
    embed = discord.Embed(title=titulo or "", description=descriçao or "", color=color)

    if campos:
        for nome, value, inline in campos:
            embed.add_field(name=nome, value=value, inline=inline)

    return embed