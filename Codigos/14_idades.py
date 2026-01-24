idades = []

aux = 0

r = input("Informe uma idade:")

while r != "":
    idades.insert(aux, r)
    #idades.append(r)
    r = input("Informe outra idade:")
    aux += 1

print("As idades são: ")
for i in idades:
    print(i)

quant = len(idades)
media = sum(idades)/quant
minimo = min(idades)
maximo = max(idades)

print("Quantidade de idades:", quant)
print("Média das idades:", media)
print("Menor idade:", minimo)
print("Maior idade", maximo)