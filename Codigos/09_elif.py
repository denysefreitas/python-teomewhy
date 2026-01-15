idade = input("Informe a sua idade: ")
idade = int(idade)

if idade >= 18 and idade < 60:
    print("Você tem", idade, "anos. Por lei, é permitida a ingestão de bebidas alcóolicas a partir dos 18. Logo, essa prática é legal. Beba com moderação!")
elif idade >= 60:
    print("Você tem", idade, "anos. Por lei, você pode consumir bebidas alcóolicas, mas não é recomendado. Repense essa decisão, sua saúde deve vir em primeiro lugar!")
else: 
    print("A ingestão de bebidas alcóolicas é permitida apenas para maiores de 18 anos", "Você tem apenas", idade, "anos de idade. Logo, é ilegal. Não beba!")