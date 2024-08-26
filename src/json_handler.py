# Importaçoes:
import json

# Manutenção de Dados:
def load_data(file):
    try:
        # Abre um ARQ (paremetro of def) and read, retornando carega_data:
        with open(file, 'r') as f:
            return load_data(f)
    except FileNotFoundError:
        return {}
    
def save_data(file, data):
    # Abre ARQ (paremetro of def) e escreve ele:
    with open(file, 'w') as f:
        # Add data com formataçao:
        json.dump(data, f, indent= 4)