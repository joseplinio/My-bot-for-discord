# Importaçoes:
from constants import DEFAULT_LEVEL, DEFAULT_HP, DEFAULT_EXP

# Class do comando Inimigo:
class Inimigo():
    def __init__(self, bot):
        self.bot = bot

    inimigo_data = {
        "name": "Monstro",
        "level": 2 * DEFAULT_LEVEL,
        "life": 2 * DEFAULT_HP,
        "max_life" : DEFAULT_LEVEL,
        "exp": DEFAULT_LEVEL * 5,
        "damege": 25,
        "class": "Inimigo"
    }
