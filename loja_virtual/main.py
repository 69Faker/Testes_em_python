class Main:
    pass

print("testandoooooo")

from cliente import Cliente
from conta import Conta

c1 = Cliente
input(("Digite seu nome:", c1.nome,"\n Digite seu telefone:", c1.telefone,"\nDigite seu cpf:", c1.cpf))
conta = Conta(c1.nome,1900,0)

print("Nome:", c1.nome, "Telefone:", c1.telefone ,"CPF:", c1.cpf)
print(conta.titular, "Número: ", conta.numero, "Seu salto:", conta.saldo)

