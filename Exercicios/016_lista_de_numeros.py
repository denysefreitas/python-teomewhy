lista = [10, 22, 11, 14, 77, 13, 90]

numero = input("Infome um número a ser buscado na lista: ")
numero = int(numero)

aux = 0

for i in range(len(lista)):
    num_lista = int(lista[i])
    if num_lista == numero:
        aux += 1

# RESOLUÇÃO DO PROF. TÉO:
# for i in lista:
# if(i == numero):
# aux +=

print("A quantidade de vezes que o número", numero, "apareceu foi:", aux)