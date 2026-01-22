saldoTotal = 0.0
v = input("Informe um valor: ")

while v != "":
    v = float(v)
    saldoTotal += v
    v = input("Informe um novo valor: ")

print("O valor total do saldo em conta é", saldoTotal)