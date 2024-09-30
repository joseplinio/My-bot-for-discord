import pytest
from src.models.player import Player
from utils.experience_system import ganhar_experiencia, calcular_proximo_xp

@pytest.fixture
def player_inicial():
    """Cria um jogador de nível inicial para os testes."""
    return Player(nome="Jogador", nivel=1, vida=100, dano=15, inventario=[], exp=1, classe="Guerreiro")

def test_ganhar_experiencia(player_inicial):
    """Testa se o jogador ganha experiência e sobe de nível corretamente."""
    # Jogador inicial deve estar no nível 1 com 0 de exp
    assert player_inicial.nivel == 1
    assert player_inicial.exp == 1

    # Ganhar 150 pontos de experiência deve fazer o jogador subir para o nível 2
    ganhar_experiencia(player_inicial, 150)
    
    assert player_inicial.nivel == 2
    assert player_inicial.exp < calcular_proximo_xp(2)  # Verifica se a exp restante é menor que a necessária para o próximo nível
    assert player_inicial.vida == player_inicial.vida_maxima  # Vida é restaurada ao subir de nível
    assert player_inicial.dano == 17  # Dano é incrementado ao subir de nível

def test_calcular_proximo_xp():
    """Testa se o cálculo de experiência para o próximo nível está correto."""
    assert calcular_proximo_xp(1) == 100
    assert calcular_proximo_xp(2) == pytest.approx(282.84, 0.1)
    assert calcular_proximo_xp(3) == pytest.approx(519.62, 0.1)

