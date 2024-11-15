quantidade = 0
soma = 0 
media = 0 
print("digite '-0' para finalizar")
valor = float(input("digite um valor:"))

while (valor > 0.0):
    soma = soma + valor
    quantidade = quantidade + 1

    valor = float(input("digite um valor:"))

media = soma / quantidade
print("\n Total da soma:", soma)
print("\n quantidade de valores digitados:", quantidade)
print("\n Média dos valores:", media)

def mensagem1():
    print("legal meu pacero")

def mensagem2():
    return "legal meu xuxu"

mensagem1()

texto = mensagem2()
print(texto)
