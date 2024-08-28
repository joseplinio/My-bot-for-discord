# Importaçoes:
from discord.ext import commands
import json
import discord
import asyncio
from src.constants import DEFAULT_HP, DEFAULT_LEVEL, DEFAULT_INVENTORY, DEFAULT_EXP

# Abrindo a confing do arquivo data:
with open('data/config.json') as config_file:
    config = json.load(config_file)

# Permisoes do bot:
intents = discord.Intents.default()
intents.message_content = True

# Criação do bot com o prefixo definido
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)


# Class of player:
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para criar um personagem:
    @commands.command(name='criar_personagem')
    async def create_character(self, ctx,):
        name = await self.pergunta_name(ctx)
        # Se nao de o TimeOutErro o if e executado se nao o else:
        if name:
            user_data = {
                "name": name,
                "level": DEFAULT_LEVEL,
                "life": DEFAULT_HP,
                "inventory": DEFAULT_INVENTORY,
                "exp": DEFAULT_EXP,
            }
            # Abre o ARQ.json e escreve nele o user_data:
            with open (f'{ctx.author.id}.json', 'w') as f:
                json.dump(user_data, f)
            await  ctx.send(f'**Personagem *{name}* criado com sucesso!**') 
        else:
            await ctx.send('**Não foi possível criar o personagem, pois nenhum nome foi fornecido.**')
        
    
    async def pergunta_name(self, ctx):
        # Lib pra validaçao de data:
        import re

        # Pergunta o nome:
        await ctx.send('**Qual vai ser o nome do seu personagem? : **')
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            response = await self.bot.wait_for('message', check=check,timeout=30.0)
            name = response.content.strip()  # Tira os espaços
            name = re.sub(r'\s+', '_', name) # Substitui os espaços por __
            sanitized_name = name.replace("<", "&lt;").replace(">", "&gt;") # Previnino contra ataque em HTML:

            # Se o nome tiver caracteris malisiosos avisa:
            if not re.match("^[A-Za-z0-9_-]*$", response.content):
                await ctx.send("Nome inválido! Use apenas letras, números, hífens e sublinhados.")
                return None
            else:
                await ctx.send(f'**Ótimo nome,** *{sanitized_name}* **!**')
                await asyncio.sleep(1.3)
                return sanitized_name
        except asyncio.TimeoutError:
            # Error por esperar:
            await ctx.send('**Você demorou muito tempo para responder.**')
            return None
        
    async def pergunta_class(self, ctx):
        lista_classes = ["Herói", "Mago", "Arqueiro", "Guerreiro"]
        
        await ctx.send('**Qual clase voce vai escolher nobre aventureiro? : **')
        
        async def menu(self, ctx):
            for idx, classe in enumerate(lista_classes, 1):
                await ctx.send(f'{idx} - {classe}')
        
        def check(m):
            m.author == ctx.author and m.channel == ctx.channel
            
        respose = await self.bot.wait_for('message', check=check,timeout=30.0)
        try:
            if respose.content.isdigit() and 1 <= int(respose.content) <= len(lista_classes):
                chosen_class = lista_classes[int(respose.content) - 1]
                await ctx.send(f'**Você escolheu a classe:** *{chosen_class}*')
                return chosen_class
            else:
                await ctx.send('Resposta inválida. Por favor, escolha um número correspondente à classe.')
                return None
        except TimeoutError:
            await ctx.send('Você demorou muito tempo para responder.')
            return None
        
            
    @commands.command(name='view_stats')
    async def view_stats(self, ctx):
        try:
            # Abre o ARQ.json so user e carega o user data:
            with open(f'{ctx.author.id}.json', 'r') as f:
                user_data = json.load(f)
            # Mostra os estatus do user:
            await ctx.send(f"**Status do Personagem:**\n"
                f"Nome: **{user_data['name']}**\n"
                f"Nível: **{user_data['level']}**\n"
                f"Vida: **{user_data['life']}**\n"
                f"Experiência: **{user_data['exp']}**")
        except FileNotFoundError:
            # Se nao tiver o ARQ.json da esse error: 
            await ctx.send('**Nenhum personagem encontrado. Por favor, crie um personagem primeiro usando o comando `!criar_personagem`.**')
        

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Player(bot))