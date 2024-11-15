arquivo = open("texto.txt", "w")
arquivo.write("laiza lindona\n")
arquivo.write("lindissima")
arquivo.close()


leitura = open("texto.txt", "r")
print(leitura.read())
leitura.close()