valorTotal = 0.0

tipoSorvete = input("""As opções de tipo de sorvete são:
    1 - casquinha
    2 - cascão
    3 - cestinha 
Informe a sua escolha: """)

if tipoSorvete == "1":
    valorTotal = 1.0
elif tipoSorvete == "3":
    valorTotal = 4.0
elif tipoSorvete == "2":
    valorTotal = 2.5

if valorTotal == 0:
    print("Não temos essa opção. Leia atentamente ao enunciado de escolha.")
else: 
    saborSorvete = input("""As opções de sabor de sorvete são:
    1 - morango
    2 - creme
    3 - chocolate 
Informe a sua escolha: """)

    if saborSorvete != "1" and saborSorvete != "2" and saborSorvete != "3":
        print("Não temos essa opção. Leia atentamente ao enunciado de escolha.")
    else: 
        cSorvete = input("""As opções de sabor da cobertura sorvete são:
    1 - caramelo
    2 - morango
    3 - chocolate
    4 - nenhuma
Informe a sua escolha: """)

        if cSorvete == "1":
            cSorvete = "de caramelo"
            valorTotal += 1.5
        elif cSorvete == "2":
            cSorvete = "de morango"
            valorTotal += 1.5
        elif cSorvete == "3":
            cSorvete = "sabor chocolate"
            valorTotal += + 1.5
        elif cSorvete == "4":
            cSorvete = "ausente"
        
        if(cSorvete != "de caramelo" and cSorvete != "de morango" and cSorvete != "de chocolate" and cSorvete != "ausente"):
            print("Não temos essa opção. Leia atentamente ao enunciado de escolha.")
        else:
            print("O valor total do pedido foi de: R$", valorTotal)

    

