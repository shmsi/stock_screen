import yaml 

def get_symbols():
    with open('symbols.yml', 'r') as f:
        return yaml.safe_load(f)

