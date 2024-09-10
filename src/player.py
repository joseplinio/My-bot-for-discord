# Importaçoes:
from discord.ext import commands
from json_handler import load_data, save_data
import random
from inimigo import Inimigo
import json
import discord
import asyncio

# Carregar as configurações do bot
with open('data/config.json') as config_file:
    config = json.load(config_file)

# Configurar as permissões e prefixo do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Class do comando Player:
class Player(commands.Cog):
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, oponente):
        dano = random.randint(0, self.ataque)
        oponente['life'] -= dano
        return dano 

class BatalhaTurno:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.turno_atual = jogador1

    async def realizar_turno(self,ctx, oponente):
        dano = self.turno_atual.atacar(oponente)        
        await ctx.send(f"{self.turno_atual.nome} atacou {oponente['name']}, causando {dano} de dano. O {oponente['name']} agora tem {oponente['life']} HP.")

        if oponente['life'] <= 0:
            await ctx.send(f"{self.turno_atual.nome} venceu a batalha e ganhou {oponente['exp']} de EXP!")
            self.jogador1['exp'] += oponente['exp']
            save_data(f'{ctx.author.id}.json', self.jogador1['exp'])
            return False # Fim da batalha
            

        self.turno_atual = self.jogador2 if self.turno_atual == self.jogador1 else self.jogador1 # entender melhor
        await ctx.send(f'Agora o turno e do jogador {self.turno_atual.nome}')
        return True # Batalha continua
        
    @commands.command(name='iniciar_batalha')
    async def init_bettla(ctx, player, inimigo):
        try:
            player_data = load_data(f'{ctx.author.id}.json', 'r') # aparente ter um erro, mas nao sei
        except FileNotFoundError:
            await ctx.send("Você ainda não criou um personagem. Use `!criar_personagem` para criar um.")
            return
        
        jogador1 = Player(player_data['name'], player_data['life'], player_data['damege'])
        inimigo = Inimigo.inimigo_data
    
        if not jogador1: # estudar melhor
            await ctx.send("Voce não possuem personagen criado, por favor crie um em `!criar_personagem`.")
            return
        
        batalha = BatalhaTurno(jogador1=jogador1, jogador2= inimigo)
        await ctx.send(f"Uma batalha começou entre {jogador1['name']} e {inimigo['name']}!")
        await ctx.send(f"Agora é o turno de {jogador1['name']}. Use o comando `!atacar` para atacar.")

        bot.batalhas[ctx.channel.id] = batalha

        batalha_continua = True
        while batalha_continua:
            batalha_continua =  await batalha.realizar_turno(ctx,inimigo)

            if not batalha_continua:
                break
            
            await ctx.send("Digite `!atacar` para atacar ou `!desistir` para tentar desistir da batalha.")
            
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['!atacar', '!desistir']
            
            try:

                response = await bot.wait_for('message', check=check,timeout=30)
                if response.content == '!atacar':
                    batalha_continua

                elif response.content == '!desistir':

                    if random.randint (1,2) % 2 == 0:
                        await ctx.send(f"{jogador1.nome} fugio da batalha!")
                        batalha_continua = False

                    else:
                        await ctx.send(f"Voce nao pode fugir da batalha! {jogador1.nome} ")    
                        batalha_continua
                    
            except asyncio.TimeoutError:
                await ctx.send("Você demorou muito para responder. A batalha continua.")
        
        # Remove a batalha do canal após o término
        bot.batalhas[ctx.channel.id, None]

# Define os comandos para o bot:
async def setup(bot):
    await bot.add_cog(Player(bot))