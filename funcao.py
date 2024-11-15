def lernotas():
    n = float(input("Digite uma nota do aluno:"))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("nota n1:", n1)
    print("nota n2:", n2)
    print("media:", media, "Resultado:", end="")
    if media < 7:
        print("reporvado")
    else:
        print("aprovado")
    
a = lernotas()
b = lernotas()
resultado(a,b)