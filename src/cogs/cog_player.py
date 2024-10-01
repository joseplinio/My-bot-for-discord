# Importaçoes:
import re
from typing import Optional
import asyncio

# Iniando a classe para a cog:
class CharacterCreation:
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
        confirm = await self.fazer_pergunta(f'**Você escolheu:** __{choice}__. **Está correto? (sim/não)**') 
        return confirm and confirm.lower().strip()[0] == "s"
    

    async def pergunta_nome(self, ctx) -> Optional[str]:
        while True:
            nome  = self.fazer_pergunta(ctx, "**Qual vai ser o nome do seu personagem?**")
            if not nome:
                return None
            
            nome_limpo = re.sub(r'\s+', '_', nome)
            nome_limpo = re.sub(r'[<>]', '', nome_limpo)

            if not re.match("^[A-Za-z0-9_-]*$", nome_limpo):
                await ctx.send("Nome inválido! Use apenas letras, números, hífens e sublinhados.")


                # tem que estudar mais para fazer as defs (a logica e facil):
                # e so colocar em pratica ;] !