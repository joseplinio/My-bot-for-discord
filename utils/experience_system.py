def ganhar_experiencia(player, quantidade: float):
    """ 
    Funçao que faz com que os parametros recebam exeperiencia
    
    param player: Um objeto que recebe uma quantidade de exp
    param quantidade: E a quantidede que o player vai receber de exp tipo: [quant = 10]
    
    """
    player.exp += quantidade
    print(f"{player.nome} ganhou {quantidade} pontos de experiência!")

    while player.exp >= calcular_proximo_xp(player.nivel):
        subir_de_nivel(player)

def calcular_proximo_xp(nivel):
    """
    Calcula o proximo nivel usando uma exepreçao matematica e retorna ela
    param nivel : E um numero e que instanciado
    """
    return 100 * (nivel ** 1.5)

def subir_de_nivel(player):
    """
    Funçao que faz o nivel aumentar, juuntamente com a vida_maxima, vida e dano
    param player: E´ um objeto que nesse caso e um classe 
    """
    player.nivel += 1
    player.exp -= calcular_proximo_xp(player.nivel - 1)

    player.vida_maxima += 10
    player.vida = player.vida_maxima
    player.dano += 2