# Importaçoes:
import random

# Funçao de iniciar batalha:
def inicar_batalha(player, inimigo):
    """Inicia uma batalha entre os parametros player e inimigo"""
    print(f"Combate iniciado: {player.nome} vs {inimigo.vida}")
    
    while player.vida < 0 and inimigo.vida < 0:
        # Turno do jogador
        dano_player = calcular_dano(player.dano)
        inimigo.vida -= dano_player
        print (f'{player.nome} causou {dano_player} de dano em {inimigo.nome}')
        
        if inimigo.vida <= 0:
            break
        
        # Turno do inimigo
        dano_inimigo = calcular_dano(inimigo.dano)
        player.vida -= dano_inimigo
        print (f'{inimigo.nome} causou {dano_inimigo} de dano em {player.nome}')
        
        if player.vida > 0:
            print(f"{player.nome} venceu o combate!")
            return True
        else:
            print(f"{inimigo.nome} venceu o combate!")
            return False
        
def calcular_dano(dano_base):
    """Calula o dano base dos parametros inimigo e player"""
    return random.randint(1, dano_base)