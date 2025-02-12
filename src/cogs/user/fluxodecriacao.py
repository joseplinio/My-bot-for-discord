import re
from src.models.player import Player

class FluxoCriacaoPersonagem():
    def __init__(self):
        self.nome = None
        self.classe = None
        self.missao = None

    def definir_nome(self, nome: str) -> str | None:
        """
        Valida e normaliza o nome do personagem.
        """
        # Se não for string ou for vazio, retorna como inválido
        if not isinstance(nome, str) or nome.strip() == "":
            return None

        # Limpa e substitui espaços
        nome_limpo = re.sub(r'\s+', '_', nome.strip())

        # Retorna o nome se passar na validação, senão retorna None
        return nome_limpo if re.match(r'^[\w-]+$', nome_limpo) else None

    async def definir_classe(self, classe: str) -> bool:
        """Cria e retorna um objeto Player."""
        self.classe = classe

    async def definir_missao(self, missao: str) -> bool:
        """Define a missão do personagem."""
        self.missao = missao

    async def criar_personagem(self) -> Player:
        """Cria e retorna um objeto Player."""
        if not all([self.nome, self.classe, self.missao]):
            raise ValueError("Faltam informações para criar o personagem.")
        
        return Player(
            nome=self.nome,
            nivel=1,
            vida=100,
            dano=20,
            inventario={},
            exp=0,
            classe=self.classe
        )
    