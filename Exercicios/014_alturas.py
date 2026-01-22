i = 0
somaAlturas = 0.0

#while i < 4:
#    altura = input("Informe uma altura: ")
#    altura = float(altura)
#    somaAlturas += altura 
#    i += 1

for i in range(4): # range(0, 4)
    altura = input("Informe uma altura: ")
    altura = float(altura)
    somaAlturas += altura 
    i += 1

print("A soma das alturas informadas é", somaAlturas)