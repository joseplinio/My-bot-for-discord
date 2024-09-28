# Importaçoes:
import random

# Funçao de iniciar batalha:
def iniciar_batalha(player, inimigo):
    """Inicia uma batalha entre os parametros player e inimigo"""
    print(f"Combate iniciado: {player.nome} vs {inimigo.nome}")
    
    while player.vida > 0 and inimigo.vida > 0:
        # Turno do jogador
        dano_player = calcular_dano(player.dano)
        inimigo.receber_dano(dano_player)
        print(f'{player.nome} causou {dano_player} de dano em {inimigo.nome}. Vida restante do inimigo: {inimigo.vida}')
        
        if inimigo.vida <= 0:
            print(f"{player.nome} venceu o combate!")
            return True
        
        # Turno do inimigo
        dano_inimigo = calcular_dano(inimigo.dano)
        player.receber_dano(dano_inimigo)
        print(f'{inimigo.nome} causou {dano_inimigo} de dano em {player.nome}. Vida restante do jogador: {player.vida}')
        
        if player.vida <= 0:
            print(f"{inimigo.nome} venceu o combate!")
            return False

def calcular_dano(dano_base):
    """Calula o dano base dos parametros inimigo e player, com variaçao"""
    return random.randint(dano_base - 2, dano_base + 2)