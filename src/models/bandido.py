# Importaçoes:
from inimigo import Inimigo
from constants import DEFAULT_HP

# Incio da class Bandido(filha):
class Bandido(Inimigo):
    # Chama o construtor da classe pai (Inimigo)
    def __init__(self, nome: str, vida: int, dano: int, exp: int):
        super().__init__(nome='Bandido', vida=DEFAULT_HP, dano=10, exp=15, descricao=self.gerar_descricao())