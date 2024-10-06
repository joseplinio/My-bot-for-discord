# Importaçoes:
import random

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

    def __init__(self, nome: str, vida: int,nivel: int, dano: int, exp: int, descricao: str = None):
        self._nome = nome
        self._nivel = max(nivel, 1) # Nivel minimo e de 1;
        self._vida_maxima = max(vida, 100) # Vida máxima mínima é 100;
        self._vida = self._vida_maxima
        self._dano = max(dano, 15)  # Dano mínimo é 15;
        self._exp = max(exp, 20)  # Experiência mínima é 20;
        self._player = None
        self._descricao = descricao if descricao else self._gerar_descricao()
        self._recompensas = self._gerar_recompensas()
        
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
    
    @property
    def nivel(self) -> int:
        return self._nivel
    
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

    @nivel.setter
    def nivel(self, novo_nivel: int) -> None:
        if novo_nivel <= 0:
            raise ValueError("O nível não pode ser negativo")
        self._nivel += random.randint(novo_nivel + 2, novo_nivel - 2)

    # Adiciona o jogador ao combate:
    def adiciona_jogador_ao_combate(self, player):
        from .player import Player
        if not isinstance(player, Player):
            raise ValueError('O objeto passado não é um Player.')
        self._player = player

    # Ataca o jogador:
    def atacar_jogador(self) -> tuple:
        """Inimigo ataca o jogador, causando dano à vida do jogador."""
        if self._player:
            dano_causado = random.randint(self._dano + 2, self._dano - 2)
            self._player.receber_dano(dano_causado)
            return self._nome, dano_causado
        else:
            raise ValueError('Nenhum jogador está em combate com este inimigo.')

    # Recebe o dano:
    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self._vida = max(self._vida - dano, 0)  # Garante que a vida não fique negativa

    # Gera um descriçao para o inimigo:
    def _gerar_descricao(self) -> str:
        """Faz com o inimigo receba uma descrição aleatoria com ações e adjetivos para a descrição"""
        adjetivo = ["feroz", "assustador", "imponente", "misterioso", "ágil"]
        acoes =  ["espreita nas sombras", "olha fixamente para você", "prepara-se para atacar", "emite um som ameaçador"]
        
        return f"Um {random.choice(adjetivo)} {self._nome} que {random.choice(acoes)}."
    
    # Gera a recompensa do inimigo:
    def _gerar_recompensas(self) -> list:
        recompensas = []
        if random.random() < 0.5:
            recompensas.append("Poção de Cura")
        
        if random.random() < 0.3:
            recompensas.append("Moeda de Ouro")
        
        if random.random() < 0.1:
            recompensas.append("Item Raro")
        
        return recompensas
    
    # Eventos:
    
    # inimigo morre:
    def morrer(self) -> tuple:
        """Retorna a experiência e as recompensas quando o inimigo morre."""
        return  self._exp, self._recompensas 
    
    # O inimigo e melhorado:
    def melhorar_inimigo(self) -> None:
        """
        Função responsável por aumentar os atributos do inimigo com base no nível do player.
        """
        if self._player is None:
            raise ValueError("Nenhum jogador está associado a este inimigo.")
        self._checar_e_ajustar_nivel()

