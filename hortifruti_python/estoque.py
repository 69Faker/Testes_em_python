class Frutas:
    def __init__(self, fruta, preco, peso):
        self.fruta = fruta
        self.valor = preco
        self.peso = peso

# Lista de frutas
frutas_info = [
    {"fruta": "Banana", "preco": 4.00, "peso": 1.0},
    {"fruta": "Maçã", "preco": 3.00, "peso": 1.0},
    {"fruta": "Pera", "preco": 4.50, "peso": 1.0}
]

# Criando instâncias da classe Frutas
frutas = [Frutas(info["fruta"], info["preco"], info["peso"]) for info in frutas_info]

def Frutas():
    x = int(input("escolha um fruta 1-3")) - 1
    pass