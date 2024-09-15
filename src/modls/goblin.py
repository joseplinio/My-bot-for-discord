# Importaçoes:
from inimigo import Inimigo
from comandos import constants

# Incio da class Goblin(filha):
class Goblin(Inimigo):
    # Chama o construtor da classe pai (Inimigo)
    def __init__(self, nome: str, vida: int, dano: int, exp: int):
        super().__init__(nome='Goblin', vida=constants.DEFAULT_HP, dano=10, exp=15)