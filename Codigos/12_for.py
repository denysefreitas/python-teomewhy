nome = "Denyse"

for i in nome:
    print(i, end = " ")

# i recebe TEMPORARIAMENTE uma atribução (na sequência de elementos de 'nome')

print("----------------")
print("Tabuada")

numero = 2
maxNumero = 100

print("Tabuada do", numero)
for i in range(1, maxNumero+1):
    print(numero, "x", i, "=", numero * i)

print("---------------------")
numero = 4

print("Tabuada do", numero)
for i in range(4, 101):
    print(numero, "x", i, "=", numero * i)

# range(min, max) é aberto em max, isto é, não o inclui