# Classe Inimigo:
class Inimigo:
    """
    Representa um inimigo no jogo.

    Atributos:
        nome (str): O nome do inimigo.
        vida (int): A quantidade de vida do inimigo.
        dano (int): O dano que o inimigo pode causar.
        exp (int): A quantidade de experiência que o inimigo fornece ao ser derrotado.
    """

    def __init__(self, nome: str, vida: int, dano: int, exp: int, descricao: str = None):
        self._nome = nome
        self._vida = max(vida, 0)  # Vida mínima é 0
        self._dano = max(dano, 0)  # Dano mínimo é 0
        self._exp = max(exp, 0)  # Experiência mínima é 0
        self._player = None
        self._descricao = descricao if descricao else self.gerar_descricao()

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
    def descricao(self) -> str:
        return self._descricao
    
    # Setters para alterar valores com validação:
    @vida.setter
    def vida(self, nova_vida: int) -> None:
        if nova_vida < 0:
            raise ValueError('A vida não pode ser negativa.')
        self._vida = nova_vida

    @dano.setter
    def dano(self, novo_dano: int) -> None:
        if novo_dano < 0:
            raise ValueError('O dano não pode ser negativo.')
        self._dano = novo_dano

    @exp.setter
    def exp(self, novo_exp: int) -> None:
        if novo_exp < 0:
            raise ValueError('A experiência não pode ser negativa.')
        self._exp = novo_exp

# Adiciona o jogador ao combate:
    def adiciona_jogador_ao_combate(self, player):
        from .player import Player
        if not isinstance(player, Player):
            raise ValueError('O objeto passado não é um Player.')
        self._player = player

    def atacar_jogador(self) -> None:
        """Inimigo ataca o jogador, causando dano à vida do jogador."""
        if self._player:
            self._player.receber_dano(self._dano)
        else:
            raise ValueError('Nenhum jogador está em combate com este inimigo.')

    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self._vida = max(self._vida - dano, 0)  # Garante que a vida não fique negativa

    def gerar_descricao(self) -> str:
        """Faz com o inimigo receba uma descrição aleatoria com ações e adjetivos para a descrição"""
        # Iportaçao:
        from random import choice
        
        adjetivo = ["feroz", "assustador", "imponente", "misterioso", "ágil"]
        acoes =  ["espreita nas sombras", "olha fixamente para você", "prepara-se para atacar", "emite um som ameaçador"]
        return f"Um {choice(adjetivo)} {self._nome} que {choice(acoes)}."