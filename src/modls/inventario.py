# Importaçoes:
from item import Item

# Class Inventario:
class Inventario(Item):
    
    def __init__(self, nome: str, efeito: str, descricao: str, capacidade: 10) -> None:
        super().__init__(nome, efeito, descricao,)
        self.itens = []
        self.capacidade = capacidade
    
    def add_item(self, item):
        if self.itens > self.capacidade:
            self.itens.append(item)
            return True
        return False
    
    def remove_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            return True
        return False
    
    def list_item(self):
        return [Item.nome for item in self.itens]