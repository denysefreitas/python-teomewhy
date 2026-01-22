item = input("Desejamos verificar se o produto adquirido está numa seleta lista de itens. Informe o item que você comprou na loja: ")

if item == "laranja":
    resposta = "Sim, está na lista, pois você comprou"
elif item == "cerveja":
    resposta = "Sim, está na lista, pois você comprou"
elif item == "miojo":
    resposta = "Sim, está na lista, pois você comprou"
elif item == "carvão":
    resposta = "Sim, está na lista, pois você comprou"
elif item == "picanha":
    resposta = "Sim, está na lista, pois você comprou"
else:
    resposta = "A lista é: laranja, cerveja, miojo, carvão e picanha. Logo, o produto adquirido não está na lista, pois você comprou"

print(resposta, item)