# Importaçoes:
from inimigo import Inimigo
from constants import DEFAULT_HP

# Incio da class Lobo(filha):
class Lobo(Inimigo):
    # Chama o construtor da classe pai (Inimigo)
    def __init__(self, nome: str, vida: int, dano: int, exp: int):
        super().__init__(nome='Lobo', vida=DEFAULT_HP, dano=15, exp=20, descricao=self.gerar_descricao())
    
    