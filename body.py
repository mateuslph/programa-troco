from decimal import Decimal

listaTrocos = []

def insereValores():
    valorCompraAux = input("Digite o valor da compra: \n")
    valorCompra = Decimal(valorCompraAux)
    valorRecebidoAux = input("Digite o valor recebido: \n")
    valorRecebido = Decimal(valorRecebidoAux)
    if (valorCompra > valorRecebido):
        print("O valor do recebido precisa ser igual ou superior ao valor de compra.")
        exit()
    return valorCompra, valorRecebido

def calculaTroco(valorCompra, valorRecebido):
    valorTroco = (valorRecebido - valorCompra)
    valorTrocoOriginal = valorTroco
    return valorTroco, valorTrocoOriginal

def calculaQntCedulasEMoedas(valorTroco):
    while (valorTroco > 0):
        if (valorTroco >= round(Decimal(200), 2)):
            listaTrocos.append("CEDULA_200")
            valorTroco -=round(Decimal(200), 2)

        elif (valorTroco >= round(Decimal(100), 2)):
            listaTrocos.append("CEDULA_100")
            valorTroco -=round(Decimal(100), 2)

        elif (valorTroco >= round(Decimal(50), 2)):
            listaTrocos.append("CEDULA_50")
            valorTroco -=round(Decimal(50), 2)

        elif (valorTroco >= round(Decimal(20), 2)):
            listaTrocos.append("CEDULA_20")
            valorTroco -=round(Decimal(20), 2)

        elif (valorTroco >= round(Decimal(10), 2)):
            listaTrocos.append("CEDULA_10")
            valorTroco -=round(Decimal(10), 2)

        elif (valorTroco >= round(Decimal(5), 2)):
            listaTrocos.append("CEDULA_5")
            valorTroco -=round(Decimal(5), 2)

        elif (valorTroco >= round(Decimal(2), 2)):
            listaTrocos.append("CEDULA_2")
            valorTroco -=round(Decimal(2), 2)

        elif (valorTroco >= round(Decimal(1), 2)):
            listaTrocos.append("MOEDA_1")
            valorTroco -=round(Decimal(1), 2)

        elif (valorTroco >= round(Decimal(0.50), 2)):
            listaTrocos.append("MOEDA_0.50")
            valorTroco -=round(Decimal(0.50), 2)

        elif (valorTroco >= round(Decimal(0.25), 2)):
            listaTrocos.append("MOEDA_0.25")
            valorTroco -=round(Decimal(0.25), 2)

        elif (valorTroco >= round(Decimal(0.10), 2)):
            listaTrocos.append("MOEDA_0.10")
            valorTroco -=round(Decimal(0.10), 2)

        elif (valorTroco >= round(Decimal(0.05), 2)):
            listaTrocos.append("MOEDA_0.05")
            valorTroco -=round(Decimal(0.05), 2)

        elif (valorTroco >= round(Decimal(0.01), 2)):
            listaTrocos.append("MOEDA_0.01")
            valorTroco -=round(Decimal(0.01), 2)

def imprimeNaTela(valorTrocoOriginal):
    print("O valor do troco é: ", valorTrocoOriginal)
    if listaTrocos.count("CEDULA_200") > 0 : print(listaTrocos.count("CEDULA_200"), "Cédula(s) de 200 reais")
    if listaTrocos.count("CEDULA_100") > 0 : print(listaTrocos.count("CEDULA_100"), "Cédula(s) de 100 reais")
    if listaTrocos.count("CEDULA_50") > 0 : print(listaTrocos.count("CEDULA_50"), "Cédula(s) de 50 reais")
    if listaTrocos.count("CEDULA_20") > 0 : print(listaTrocos.count("CEDULA_20"), "Cédula(s) de 20 reais")
    if listaTrocos.count("CEDULA_10") > 0 : print(listaTrocos.count("CEDULA_10"), "Cédula(s) de 10 reais")
    if listaTrocos.count("CEDULA_5") > 0 : print(listaTrocos.count("CEDULA_5"), "Cédula(s) de 5 reais")
    if listaTrocos.count("CEDULA_2") > 0 : print(listaTrocos.count("CEDULA_2"), "Cédula(s) de 2 reais")

    if listaTrocos.count("MOEDA_1") > 0 : print(listaTrocos.count("MOEDA_1"), "Moeda(s) de 1 real")
    if listaTrocos.count("MOEDA_0.50") > 0 : print(listaTrocos.count("MOEDA_0.50"), "Moeda(s) de 50 centavos")
    if listaTrocos.count("MOEDA_0.25") > 0 : print(listaTrocos.count("MOEDA_0.25"), "Moeda(s) de 25 centavos")
    if listaTrocos.count("MOEDA_0.10") > 0 : print(listaTrocos.count("MOEDA_0.10"), "Moeda(s) de 10 centavos")
    if listaTrocos.count("MOEDA_0.05") > 0 : print(listaTrocos.count("MOEDA_0.05"), "Moeda(s) de 5 centavos")
    if listaTrocos.count("MOEDA_0.01") > 0 : print(listaTrocos.count("MOEDA_0.01"), "Moeda(s) de 1 centavo")
