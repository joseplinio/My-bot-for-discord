# Importaçoes:
import re
from typing import Optional
import asyncio
import discord
from utils.interatividade.funcoes_for_bot.embed_utils import criar_embed
import traceback

# Iniciaando a classe para a cog:
class MetodosCriarPersonagem():
    def __init__(self, bot):
        self.bot = bot
       
    async def fazer_pergunta(self, interaction: discord.Interaction , pertunta: str, timeout: float = 30.0) -> Optional[str]:
        try:
            # Caso ja nao tenha sido respondida sinalisa para o discord que a 
            # resposta esta sendo pertaprada:
            if not interaction.response.is_done():
                await interaction.response.defer(ephemeral=True)

            # Faz a pergunta para o player:
            await interaction.followup.send(embed=criar_embed(
                descricao=pertunta,
                color=discord.Color.dark_green()
                ),
                ephemeral=True
            )

            # Analisa que clicou a mensagem:
            def check(m):
                return interaction.user == m.author and interaction.channel == m.channel

            try:
                # Pegua a responsta do user, de forma formatada:
                response = await self.bot.wait_for('message', check=check, timeout=timeout)
                return response.content.strip()

            # Erro de tempo para caso nem ter uma resposta com mensegem:     
            except asyncio.TimeoutError():
                await interaction.response.send_message(criar_embed(
                    descricao="**Você demorou muito tempo para responder.**",
                    color=discord.Color.dark_red()
                    ),
                    ephemeral=True
                )
                return None
        
        except Exception:
            print(traceback.format_exc())
            
    # Funçao para confirmaçao de dados, retornado com formataçao sem espasos e
    # em letras minusculas, e verifica se a confirmaçao nao foi passada:
    async def confirmar_pergunta(self, interaction: discord.Interaction, choice: str) -> bool:
    
        confirmar =  await self.fazer_pergunta(interaction, f'Você escolheu: **{choice}**. Está correto? **(sim/não)**')
        if confirmar is None:
            return False
        return confirmar.lower().strip() == "s"

    # Funçao para perguntar o nome do user:
    async def pergunta_nome(self, interaction: discord.Interaction) -> str:
        try:
            while True:
            
                # Resposta do user sendo guardada em uma varievel, com validaçao para
                # caso nao tiver nada:
                nome = await self.fazer_pergunta(interaction, "*Qual vai ser o nome do seu personagem?*")
                if not nome:
                    return None
                
                # Limpando o nome:
                nome_limpo = re.sub(r'\s+', '_', nome)
                nome_limpo = re.sub(r'[<>]', '', nome_limpo)

                # Erro no nome para pervinir de ataques:
                if not re.match("^[A-Za-z0-9_-]*$", nome_limpo):
                    await interaction.followup.send(embed=criar_embed(
                        descricao="**Nome inválido! Use apenas letras, números, hífens e sublinhados.**",
                        color=discord.Color.dark_red()
                        ),
                        ephemeral=True
                    )
                    continue
                
                # Fasendo a pergunta de confirmaçao da resposta do user, retornando 
                # o nome dele se a resposta for sim, se nao so vola para o inicio do 
                # wilhe:
                if await self.confirmar_pergunta(interaction, nome_limpo):
                    await interaction.followup.send(embed=criar_embed(
                        descricao=f'Ótimo nome, **{nome_limpo} !**',
                        color=discord.Color.dark_green()
                        ),
                        ephemeral=True
                    )
                    await asyncio.sleep(1.5)
                    return nome_limpo
                 
        except Exception:
            print(traceback.format_exc())
    
    async def perguntar_classe(self, interaction: discord.Interaction) -> str:
        pass