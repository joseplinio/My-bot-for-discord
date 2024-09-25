# Importaçoes:
import random

class ScenarioGenerator:
    def __init__(self) -> None:
        self.local = [
            "Floresta Sombria", "Caverna Profunda", "Montanha Nevada",
            "Deserto Escaldante", "Pântano Nebuloso", "Ruínas Antigas"
        ]
        self.condicao = ["ensolarado", "chuvoso", "nublado", "tempestuoso", "nevando"]
        self.hora_do_dia = ["amanhecer", "meio-dia", "entardecer", "noite"]

    def generate_scenario(self):
        local = random.choice(self.local)
        condicao = random.choice(self.condicao)
        hora = random.choice(self.hora_do_dia)
        
        description = f"Você se encontra em {local}. O clima está {condicao} e é {hora}."
        return description
