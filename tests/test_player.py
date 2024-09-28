import pytest
from src.models.player import Player
from src.models.inimigo import Inimigo

@pytest.fixture
def player():
    """Cria uma instância de Player para ser usada nos testes."""
    return Player("Herói", 1, 200, 20, [], 50, "Guerreiro")

@pytest.fixture
def inimigo():
    """Cria uma instância de Inimigo para ser usada nos testes."""
    return Inimigo("Goblin", 100, 15, 50)

# Teste para verificar se os atributos iniciais são corretamente configurados
def test_atributos_iniciais(player):
    assert player.nome == "Herói"
    assert player.nivel == 1
    assert player.vida == 200
    assert player.vida_maxima == 200
    assert player.dano == 20
    assert player.exp == 50
    assert player.classe == "Guerreiro"
    assert player.inventario == []

# Teste para validar se o setter de vida está funcionando corretamente
def test_set_vida(player):
    player.vida = 150
    assert player.vida == 150

    player.vida = 250  # Vida não pode exceder a vida máxima
    assert player.vida == player.vida_maxima

# Teste para garantir que uma exceção seja lançada se o valor de vida for inválido
def test_set_vida_invalida(player):
    with pytest.raises(ValueError):
        player.vida = -10

# Teste para validar o setter de vida máxima e ajustar a vida atual
def test_set_vida_maxima(player):
    player.vida_maxima = 150
    assert player.vida_maxima == 150
    assert player.vida == 150  # Vida é ajustada para não exceder a nova vida máxima

# Teste para verificar se o jogador pode atacar o inimigo corretamente
def test_atacar_inimigo(player, inimigo):
    vida_inicial = inimigo.vida
    player.atacar_inimigo(inimigo)
    assert inimigo.vida == vida_inicial - player.dano

# Teste para garantir que o jogador receba dano corretamente
def test_receber_dano(player):
    vida_inicial = player.vida
    player.receber_dano(50)
    assert player.vida == vida_inicial - 50

    player.receber_dano(300)  # Dano maior que a vida restante
    assert player.vida == 0  # Vida não pode ser negativa

# Teste para garantir que o setter de nível esteja funcionando corretamente
def test_set_nivel(player):
    player.nivel = 5
    assert player.nivel == 5

    with pytest.raises(ValueError):
        player.nivel = 0  # O nível não pode ser menor ou igual a 0

# Teste para validar o setter de dano
def test_set_dano(player):
    player.dano = 30
    assert player.dano == 30

    with pytest.raises(ValueError):
        player.dano = -5  # Dano não pode ser negativo

# Teste para validar o setter de experiência
def test_set_exp(player):
    player.exp = 100
    assert player.exp == 100

    with pytest.raises(ValueError):
        player.exp = -20  # Experiência não pode ser negativa
