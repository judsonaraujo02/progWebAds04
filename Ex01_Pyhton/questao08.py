qtdMoeda1Cent = float(input("Digite a quantidade de moedas de 1 centavo:  "))
qtdMoeda5Cent = float(input("Digite a quantidade de moedas de 5 centavos:  "))
qtdMoeda10Cent = float(input("Digite a quantidade de moedas de 10 centavos:  "))
qtdMoeda25Cent = float(input("Digite a quantidade de moedas de 25 centavos:  "))
qtdMoeda50Cent = float(input("Digite a quantidade de moedas de 50 centavo:  "))
qtdMoeda1Real = float(input("Digite a quantidade de moedas de 1 real:  "))

total1Cent = (qtdMoeda1Cent/100)
total5Cent = (qtdMoeda5Cent/20)
total10Cent = (qtdMoeda10Cent/10)
total25Cent = (qtdMoeda25Cent/4)
total50Cent = (qtdMoeda50Cent/2)
total1Real = (qtdMoeda1Real/1)

valorTotalEconomizado = (total1Cent + total5Cent + total10Cent + total25Cent + total50Cent + total1Real)
print("   ")
print("Valor economizado em reais: ", valorTotalEconomizado)