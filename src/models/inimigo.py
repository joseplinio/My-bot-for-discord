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
        self._vida = self._vida_maxima # vida e igual a vida_maxima
        self._dano = max(dano, 15)  # Dano mínimo é 15;
        self._exp = max(exp, 20)  # Experiência mínima é 20;
        self._player = None # No inicio ele nao existe;
        self._descricao = descricao if descricao else self._gerar_descricao() # Gerar a descriçao;
        self._recompensas = self._gerar_recompensas()
        self._morto = False # Inimigo vivo no incio.
        
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
    def descricao(self) -> str:
        return self._descricao
    
    @property
    def nivel(self) -> int:
        return self._nivel
    
    @property
    def esta_morto(self) -> bool:
        return self._morto
    
    @property
    def recompensas(self) -> list:
        return self._recompensas.copy()
    
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
            raise ValueError("O nível não pode ser negativo ou zero.")
        self._nivel = novo_nivel

    @esta_morto.setter
    def esta_morto(self, valor: bool) -> None:
        if not  isinstance(valor, bool):
            raise ValueError("O valor de 'esta_morto deve ser do tipo booleano.")
        self._morto = valor
        
    # Funços para o inimigo:

    # Adiciona o jogador ao combate:
    def adicionar_jogador_ao_combate(self, player):
        from .player import Player
        if not isinstance(player, Player):
            raise ValueError('O objeto passado não é um Player.')
        self._player = player

    # Ataca o jogador:
    def atacar_jogador(self, player) -> tuple:
        """Inimigo ataca o jogador, causando dano à vida do jogador."""
        if self.esta_morto:
           raise ValueError('O Inimigo esta morto.')
        
        if self._player is None:
            self._player = player

        if self._player != player:
            raise ValueError('Nenhum jogador está em combate com este inimigo.')
        
        self._player.receber_dano(self.dano)
        
        return self.nome, self.dano 

        
            
    # Recebe o dano:
    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if self.esta_morto:
            return
        
        if self.vida == 0:
            self.esta_morto = True
        
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self.vida = max(self.vida - dano, 0)  # Garante que a vida não fique negativa

        

    # Gera um descriçao para o inimigo:
    def _gerar_descricao(self) -> str:
        """Faz com o inimigo receba uma descrição aleatoria com ações e adjetivos para a descrição"""
        adjetivo = ["feroz", "assustador", "imponente", "misterioso", "ágil"]
        acoes =  ["espreita nas sombras", "olha fixamente para você", "prepara-se para atacar", "emite um som ameaçador"]
        
        return f"o(a) {random.choice(adjetivo)} {self.nome} que {random.choice(acoes)}."
    
    # Gera a recompensa do inimigo:
    def _gerar_recompensas(self) -> list:
        """Rotorna uma lista de items que podem serem dropasdos pelo inimio"""
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
        if hasattr(self, "_morto") and self._morto:
            return 0, []
        
        self.esta_morto = True

        return self.exp, self.recompensas
    
    # O inimigo e melhorado:
    def melhorar_inimigo(self) -> None:
        """
        Função responsável por aumentar os atributos do inimigo com base no nível do player.
        """
        if self._player is None:
            raise ValueError("Nenhum jogador está associado a este inimigo.")
        self.checar_e_ajustar_nivel()

    # Checha se pode melhorar o inimigo:
    def checar_e_ajustar_nivel(self) -> None:
        """
        Verifica o nível do player e ajusta os atributos do inimigo de forma proporcional.
        """
        while self._player._nivel >= self._nivel:
            self._nivel += 1
            self._vida_maxima += self._player._nivel * 120  
            self._dano += self._player._nivel + 5
            self._exp += self._player._nivel + 10
        self._vida = self._vida_maxima
        
