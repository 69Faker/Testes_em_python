print("------Bem Vindo------")

from cliente import Clientes
from estoque import Frutas

def escolha():

    while True:
        try:
                opcao = int(input("digite entre 1-3"))
                if opcao < 1 or opcao > 3:
                    print("digite novamente")
                else:
                    escolhas(opcao)
                    break
        except ValueError:
            print("invalido")
        

def escolhas(opcao):
    match opcao:
        case 1:
            print("Frutas")
            Frutas()
        case 2:
            print("Cupons")
        case 3:
            print("Suporte")
        case 4:
            print("Carrinho")

if __name__ == "__main__":
    escolha()