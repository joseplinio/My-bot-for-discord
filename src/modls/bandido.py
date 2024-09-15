# Importaçoes:
from inimigo import Inimigo
from comandos import constants

# Incio da class Bandido(filha):
class Bandido(Inimigo):
    # Chama o construtor da classe pai (Inimigo)
    def __init__(self, nome: str, vida: int, dano: int, exp: int):
        super().__init__(nome='Bandido', vida=constants.DEFAULT_HP, dano=10, exp=15)