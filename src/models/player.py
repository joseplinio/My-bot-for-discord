#Importaçoes:
from .inimigo import Inimigo

# Classe Player:
class Player:
    """
    Representa um player no jogo.

    Atributos:
        nome (str): O nome do player.
        vida (int): A quantidade de vida do player.
        dano (int): O dano que o player pode causar.
        inventario (list): O inventario do player para carregar os itens.
        exp (int): A quantidade de experiência que o player possui.
        classe (str): A classe do player (ex.: Guerreiro, Mago).
    """

    def __init__(self, nome: str, nivel: int, vida: int, dano: int, inventario: list, exp: int, classe: str):
        self._nome = nome
        self._inventario = inventario
        self._nivel = nivel
        self._vida_maxima = max(vida, 100) # Vida máxima mínima é 100
        self._vida = self._vida_maxima  # Vida inicial é igual à vida máxima
        self._dano = max(dano, 15)  # Dano mínimo é 15
        self._exp = max(exp, 1)  # Experiência mínima é 1
        self._classe = classe
    
    # Getters para acessar os atributos de forma controlada:
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def vida(self) -> int:
        return self._vida
    
    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima
    
    @property
    def dano(self) -> int:
        return self._dano

    @property
    def exp(self) -> int:
        return self._exp

    @property
    def inventario(self) -> list:
        return self._inventario
    
    @property
    def classe(self) -> str:
        return self._classe
    
    @property
    def nivel(self) -> int:
        return self._nivel

    # Setters para alterar valores com validação:
    @vida.setter
    def vida(self, nova_vida: int):
        if nova_vida < 0:
            raise ValueError('A vida não pode ser negativa.')
        self._vida = min(nova_vida, self._vida_maxima) # Limita a vida atual à vida máxima
    
    @vida_maxima.setter
    def vida_maxima(self, nova_vida_maxima: int):
        if nova_vida_maxima < 0:
            raise ValueError('A vida não pode ser negativa.')
        self._vida_maxima = nova_vida_maxima
        self._vida = min(self._vida, self._vida_maxima)
    
    @dano.setter
    def dano(self, novo_dano: int):
        if novo_dano < 0:
            raise ValueError('O dano não pode ser negativo.')
        self._dano = novo_dano

    @exp.setter
    def exp(self, novo_exp: int):
        if novo_exp < 0:
            raise ValueError('A experiência não pode ser negativa.')
        self._exp = novo_exp

    @nivel.setter
    def nivel(self, novo_nivel: int):
        if novo_nivel <= 0:
            raise ValueError('O nivel não pode ser negativo.')
        self._nivel = novo_nivel

    # Atacar o inimigo:
    def atacar_inimigo(self, inimigo: Inimigo) -> None:
        """Jogador ataca o inimigo, causando dano à vida do inimigo."""
        if not isinstance(inimigo, Inimigo):
            raise ValueError('Nenhum jogador está em combate com este inimigo.')
        inimigo.receber_dano(self._dano)

    # receber dano do inimigo:
    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self._vida = max(self._vida - dano, 0)  # Garante que a vida não fique negativa

    # Calcula o proximo exp:
    def _calcular_exp_proximo_nivel (self) -> float:
        """
        Calcula a procima experiencia necessaria para o proximo nivel, com uma formula:
            exp.necessaria = 100 x (x^1,5)
        """
        return  100 * (self.nivel ** 1.5)
    
    # Aumenta a exp do player:
    def ganhar_exp(self, quantide: float) -> None:
        """"""
        self.exp += max(quantide, 0) # Se nao retorna o exp retorna 0
        self._checar_level_up
    
    # Checa se o player pode suber de nivel:
    def _checar_level_up(self) -> None:
        """"""
        while self.exp >= self._calcular_exp_proximo_nivel:
            self.exp -= self._calcular_exp_proximo_nivel
            self.nivel += 1
            self._aumentar_stats()
            self._calcular_exp_proximo_nivel = self._calcular_exp_proximo_nivel()

    # Aumenta os status do player:
    def _aumentar_status(self) -> None:
        """"""
        self._vida_maxima += 20
        self._vida = self.vida_maxima
        self._dano += 5        

