palavra = input("Informe uma palavra: ")

i = 0
letra = "a"

for aux in palavra:
    if aux == "a":
        i+=1

print("A letra", letra, "aparece", i, "vez(es) na palavra", palavra)