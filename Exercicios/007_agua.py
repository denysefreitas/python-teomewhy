garrafa = input("""Escolha o número corresponde à garrafa de água desejada: 
                1 - água natural 
                2 - água com gás""")

valorTotal = 0.0

if garrafa == "1":
    valortotal = 1.5
elif garrafa == "2":
    valorTotal = 2.5

if valorTotal == 0:
    print("Não temos essa opção. Leia atentamente ao enunciado de escolha.")
else:
    print("Valor total:", valorTotal)