import pytest
from src.models.player import Player
from src.models.inimigo import Inimigo
from utils.combat_system import iniciar_batalha

# Fixture para o jogador
@pytest.fixture
def player_forte():
    """Cria um player forte para os testes."""
    return Player(nome="Herói", nivel=10, vida=150, dano=30, inventario=[], exp=100, classe="Guerreiro")

@pytest.fixture
def player_fraco():
    """Cria um player fraco para os testes."""
    return Player(nome="Herói", nivel=1, vida=50, dano=10, inventario=[], exp=10, classe="Guerreiro")

# Fixture para o inimigo
@pytest.fixture
def inimigo_forte():
    """Cria um inimigo forte para os testes."""
    return Inimigo(nome="Dragão", vida=200, dano=40, exp=300)

@pytest.fixture
def inimigo_fraco():
    """Cria um inimigo fraco para os testes."""
    return Inimigo(nome="Goblin", vida=50, dano=5, exp=20)

# Teste para quando o jogador vence a batalha
def test_player_vence(player_forte, inimigo_fraco):
    resultado = iniciar_batalha(player_forte, inimigo_fraco)
    assert resultado == True  # O jogador deve vencer

# Teste para quando o inimigo vence a batalha
def test_inimigo_vence(player_fraco, inimigo_forte):
    resultado = iniciar_batalha(player_fraco, inimigo_forte)
    assert resultado == False  # O inimigo deve vencer

