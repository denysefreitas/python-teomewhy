# %%
idades = [11, 97, 10, 19, 29]
print(idades)

#soma = 0
#soma = int(soma)
#for i in range(5):
#    soma += int(idades[i])
#print("A soma das idades é:", soma)

print("A soma das idades é:", sum(idades))
print("A quantidade de idades é:", len(idades))
print("A média aritmética das idades é:", sum(idades)/len(idades))
print("A menor idade é:", min(idades))
print("A maior idade é:", max(idades))

print("----------------")

# lista = [Nome, sobrenome, é maior de idade?, idade, estado]
denyse = ["Denyse", "Freitas", True, 20, "Minas Gerais"]

# Retorna o tipo da variável
print(type(denyse)) 
print("----------------")

for i in range(5):
    print(denyse[i])

print("----------------")

denyse = ["Denyse", 
          "Freitas",
            20, 
            "Minas Gerais",
            ["A", "B", "C"]]

# Exibe o tamanho da lista
print(len(denyse))

# Exibe cada elemento da lista interna
for i in range(3):
    print(denyse[-1][i])
    # Usar a posição 'len(denyse) - 1' é o mesmo que usar diretamente o '-1'
    # Ambos garantem que, independente do tamanho da lista, será usada a última posição dela (que contém a informação desejada)

print("-------------------")

print(denyse[:2])
# Exibe denyse[0] e denyse[1], pois o intervalo é ABERTO no final

print(denyse[4][1:3])
print(denyse[4][-2:])
# Elementos do -2 até o final da lista (0)
# O zero também é FACULTATIVO no início 
# lista[start : stop : step]