#Importaçoes:
from .inimigo import Inimigo

# Classe Player:
class Player:
    """
    Representa um player no jogo.

    Atributos:
        nome (str): O nome do player;
        nivel (int): Nivel do player;
        vida (int): A quantidade de vida do player;
        dano (int): O dano que o player pode causar;
        inventario (dict): O inventario do player para carregar os itens;
        exp (int): A quantidade de experiência que o player possui;
        classe (str): A classe do player (ex.: Guerreiro, Mago).
    """

    def __init__(self, nome: str, nivel: int, vida: int, dano: int, inventario: dict, exp: int, classe: str):
        self._nome = nome # Uma String;
        self._inventario = inventario # Um dicionario;
        self._nivel = max(nivel, 1) # Nivel minimo é 1;
        self._vida_maxima = max(vida, 100) # Vida máxima mínima é 100;
        self._vida = self._vida_maxima  # Vida inicial é igual à vida máxima;
        self._dano = max(dano, 15)  # Dano mínimo é 15;
        self._exp = max(exp, 0)  # Experiência mínima é 0;
        self._classe = classe # Classe e igual e classe ;]
       
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

    # Funços para o objeto player:

    # Atacar o inimigo:
    def atacar_inimigo(self, inimigo: Inimigo) -> tuple:
        """Jogador ataca o inimigo, causando dano à vida do inimigo."""
        if not isinstance(inimigo, Inimigo):
            raise ValueError('O objeto passado não é um inimigo válido.')
        
        if inimigo.esta_morto:
            print("O inimigo ja esta morto")
            return

        if inimigo._player is None:
            inimigo.adicionar_jogador_ao_combate(self)

        if inimigo._player != self:
            raise ValueError("Nenhum jogador está em combate com este inimigo.")
        
        inimigo.receber_dano(self.dano)

    # receber dano do inimigo:
    def receber_dano(self, dano: int) -> None:
        """O inimigo recebe dano e reduz a quantidade de vida."""
        if dano < 0:
            raise ValueError('Dano não pode ser negativo.')
        self._vida = max(self.vida - dano, 0)  # Garante que a vida não fique negativa

    # Calcula o proximo exp:
    def calcular_exp_proximo_nivel (self) -> float:
        """
        Calcula a procima experiencia necessaria para o proximo nivel, com uma formula:
            exp.necessaria = 100 x (x^1,5)
        """
        return  100 * (self._nivel ** 1.5)
    
    # Aumenta a exp do player:
    def ganhar_exp(self, quantidade: float) -> None:
        """
        Funçao que adiciona uma quantidade de experiencia ao player, e chama o
        checar o proximo nivel para checar o proximo nivel

        param quantidade: tipo o self._exp (do inimigo) 
        
        """
        
        self.exp += max(quantidade, 0) # Se nao retorna o exp retorna 0
        self._checar_level_up()
    
    # Checa se o player pode suber de nivel:
    def _checar_level_up(self) -> None:
        """
        Funçao para verificar o nivel do player sendo que se sua experiencia for 
        maior ou igual ao resultado da funçao ``_calcular_exp_proximo_nivel`` ele vai
        aulmentar o nivel do player, e aulmentar os estados com o a funçao ``_aumentar_stats()``
        """
        while self.exp >= self.calcular_exp_proximo_nivel():
            self.exp -= self.calcular_exp_proximo_nivel()
            self.nivel += 1
            self.aumentar_status()

    # Aumenta os status do player:
    def aumentar_status(self) -> None:
        """
        Funçao responsavel por almentar os atributos do player sendo a vida_maxima,
        vida, dano.
        """
        self._vida_maxima += 20
        self._vida = self.vida_maxima
        self._dano += 5        
        self.calcular_exp_proximo_nivel()

    # Mexer com o sistema de inventario:

    # Adicionar o item no inventaio:
    def add_item(self, item: str) -> None:
        """
        Funçao que adiciona o item no inventario do player, com validaçoa do item
            param item (str) 
        """
        if item in self.inventario:
            self.inventario[item] += 1

        self.inventario[item] = 1

    # Exibi inventario:
    def exibir_inventario(self) -> str:
        if not self.inventario:
            return "Vazio"
        
        # entender o que acontece aqui:
        # return ", ".join(f"{item} ({quantidade})" if )

    # Remover o item do inventaio:
    def remove_item(self, item: str) -> None:
        """
        Funçao que remove o item do inventario, que valida se o item ta no inventario
        se sim so´ removo, se não da mensagem de erro
        """
        if not item in self._inventario:
            print(f"Você não possui {item} no seu inventário.")
        self._inventario.remove(item)

    # Usa um determindo item:
    def usar_item(self, item: str) -> str:
        """
        Funçao que usa o item, e verifica o item no no self._inventario retornando
        um erro ou nao dependo do modo:
            param item (str)
        """
        if not item in self._inventario:
            return f"Você não possui {item} no seu inventário."
        
        if item == "Poção de Cura":
            cura = 50
            self._vida = min(self._vida + cura, self._vida_maxima)
            self._inventario.remove(item)
            return f"Você usou uma Poção de Cura e recuperou {cura} de vida"
        
        if item == "Poção de Cura Melhorada":
            cura = 100
            self._vida = min(self._vida + cura, self._vida_maxima)
            self._inventario.remove(item)
            return f"Você usou uma Poção de Cura Melhorada e recuperou {cura} de vida"
        
        return f"Você não pode usar {item}"
        