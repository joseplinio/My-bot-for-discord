# Importaçoes:
import json

# Manutenção de Dados:
def load_data(file):
    try:
        with open(file, 'r') as f:
            return load_data(f)
    except FileNotFoundError:
        return {}
    
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent= 4)