# Importaçoes: 
from inimigo import Inimigo
from constants import DEFAULT_HP

# Incio da class InimigoVoador(filha):
class InimigoVoador(Inimigo):
    """
    Representa um inimigo no jogo.

    Atributos:
        nome (str): O nome do inimigo.
        vida (int): A quantidade de vida do inimigo.
        dano (int): O dano que o inimigo pode causar.
        exp (int): A quantidade de experiência que o inimigo fornece ao ser derrotado.
        altura_do_voo (int): A altura que o inimigo voador está.
    """
    # Chama o construtor da classe pai (Inimigo)
    def __init__(self, nome: str, vida: int, dano: int, exp: int, altura_de_voo: int):
        super().__init__(nome='Dragao', vida=DEFAULT_HP, dano=25, exp=30)
        self._altura_de_voo = max(altura_de_voo, 0)

    # Getters para acessar os atributos de forma controlada:  
    @property
    def altura_de_voo(self) -> int:
        return self._altura_de_voo
    
    # Setters para alterar valores com validação:
    @altura_de_voo.setter
    def altura_de_voo(self, nova_altura) -> None:
        if nova_altura < 0:      
            raise ValueError('A altura nao pode ser negativa.')
        self._altura_de_voo = nova_altura

