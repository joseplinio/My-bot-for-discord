# Class Player:
class Player:
    """
    Representa um player no jogo.

    Atributos:
        nome (str): O nome do inimigo.
        vida (int): A quantidade de vida do inimigo.
        dano (int): O dano que o inimigo pode causar.
        exp (int): A quantidade de experiência que o inimigo fornece ao ser derrotado.
    """
    def __init__(self, nome: str, vida: int, dano: int, exp: int, classe: str):
        self._nome = nome
        self._vida = max(vida, 0)   
        self._dano = max(dano, 0)
        self._exp = max(exp, 0)
        self._clsse = classe
    
    # Getters para acessar os atributos de forma controlada:
    def get_nome(self) -> str:
        return self._nome 
    
    def get_vida(self) -> int:
        return self._vida
    
    def get_dano(self) -> int:
        return self._dano
    
    def get_exp(self) -> int:
        return self._exp
    
    def get_classe(self) -> str:
        return self._clsse

    # Setters para alterar valores com validação   
    def set_vida(self, nova_vida: int):
        if self._vida <= 0:
            self._vida = nova_vida
        else:
            raise ValueError ('A vida não pode ser negativa.')
            
    def set_dano(self, nova_dano: int):
        if self._vida <= 0:
            self._vida = nova_dano
        else:
            raise ValueError ('A dano não pode ser negativa.')
        
    def set_exp(self, novo_exp: int):
        if self._exp <= 0:
            self._exp = novo_exp
        else:
            raise ValueError('O exp não pode ser negativa.')

