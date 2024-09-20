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
        exp (int): A quantidade de experiência que o player possui.
        classe (str): A classe do player (ex.: Guerreiro, Mago).
    """

    def __init__(self, nome: str, vida: int, dano: int, exp: int, classe: str):
        self._nome = nome
        self._vida = max(vida, 0)  # Vida mínima é 0
        self._dano = max(dano, 0)  # Dano mínimo é 0
        self._exp = max(exp, 0)  # Experiência mínima é 0
        self._classe = classe
    
    # Getters para acessar os atributos de forma controlada:
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def vida(self) -> int:
        return self._vida

    @property
    def dano(self) -> int:
        return self._dano

    @property
    def exp(self) -> int:
        return self._exp

    @property
    def classe(self) -> str:
        return self._classe

    # Setters para alterar valores com validação:
    @vida.setter
    def vida(self, nova_vida: int):
        if nova_vida < 0:
            raise ValueError('A vida não pode ser negativa.')
        self._vida = nova_vida

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

    # Atacar o inimigo:
    def atacar_inimigo(self, inimigo: Inimigo) -> None:
        """Jogador ataca o inimigo, causando dano à vida do inimigo."""
        if not isinstance(inimigo, Inimigo):
            raise ValueError('Nenhum jogador está em combate com este inimigo.')
        inimigo.receber_dano(self._dano)

    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self._vida = max(self._vida - dano, 0)  # Garante que a vida não fique negativa