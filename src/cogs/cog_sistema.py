# Importaçoes:
import re
from typing import Optional
import asyncio
import discord
from utils.embed_utils import criar_embed

# Iniando a classe para a cog:
class MetosCriarPersonagem():
    def __init__(self, bot):
        self.bot = bot

    async def fazer_pergunta(self, ctx, pergunta: str, timeout: float = 30.0) -> Optional[str]:
        await ctx.send(pergunta)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            response = await self.bot.wait_for("message", check=check, timeout=timeout)
            return response.content.strip()
        except asyncio.TimeoutError:
            await ctx.send("**Você demorou muito tempo para responder.**")
            return None
    
    async def confirma_escolha(self, ctx, choice: str) -> bool:
        confirm = await self.fazer_pergunta(ctx, f'Você escolheu: **{choice}**. Está correto? **(sim/não)**') 
        return confirm and confirm.lower().strip()[0] == "s"
    

    async def pergunta_nome(self, ctx) -> Optional[str]:
        while True:
            
            await ctx.send(embed=criar_embed(
                color=discord.Color.dark_green(),
                campos=[
                    ["*Qual vai ser o nome do seu personagem?*", "", True]
                ]
            ))

            nome  =  await self.fazer_pergunta(ctx, "Sua escolha:")
            if not nome:
                return None
            
            nome_limpo = re.sub(r'\s+', '_', nome)
            nome_limpo = re.sub(r'[<>]', '', nome_limpo)

            if not re.match("^[A-Za-z0-9_-]*$", nome_limpo):
                await ctx.send("**Nome inválido! Use apenas letras, números, hífens e sublinhados.**")
                continue
            
            if await self.confirma_escolha(ctx, nome_limpo):
                await ctx.send(f'Ótimo nome, **{nome_limpo} !**')
                await asyncio.sleep(1.5)
                return nome_limpo


    async def pergunta_classe(self, ctx) -> Optional[str]:
        lista_de_classes = ["Herói", "Mago", "Arqueiro", "Guerreiro"]

        def menu():
            return "\n".join(f"**{idx}** - **{classe}**" for idx, classe in enumerate(lista_de_classes, 1))      
        
        while True:
            
            await ctx.send(embed=criar_embed(
                color=discord.Color.dark_green(),
                campos=[
                    ["*Qual classe você vai escolher, nobre aventureiro?*", menu(), True]
                ]
            ))
            
            escolha =  await self.fazer_pergunta(ctx, "Digite o número correspondente à classe:")
            if  not escolha:
                return None

            if escolha.isdigit() and 1 <= int(escolha) <= len(lista_de_classes):
                classe_escolhida = lista_de_classes[ int(escolha) - 1]
                
                if await self.confirma_escolha(ctx, classe_escolhida):
                    await ctx.send(f'Sua classe escolhida é **{classe_escolhida}** .')
                    await asyncio.sleep(1.5)
                    return classe_escolhida
                
            else:
                await ctx.send('**Resposta inválida. Por favor, escolha um número correspondente à classe.**')
                await asyncio.sleep(1.5)
                