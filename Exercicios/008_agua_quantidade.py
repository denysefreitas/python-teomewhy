valorTotal = 0.0
garrafa = input("""Escolha o número corresponde à garrafa de água desejada: 
                1 - água natural 
                2 - água com gás""")

n = input("Informe a quantidade de água com gás que você deseja: ")
n = int(n)

if (garrafa == "1"):
    valorTotal =  1.5 * n
elif(garrafa == "2"):
    valorTotal = 2.5 * n

if valorTotal == 0.0:
    print("Não temos essa opção. Leia atentamente ao enunciado de escolha.")
else:
    print("Valor total:", valorTotal)