import body

valorCompra, valorRecebido = body.insereValores()
valorTroco, valorTrocoOriginal = body.calculaTroco(valorCompra, valorRecebido)
body.calculaQntCedulasEMoedas(valorTroco)
body.imprimeNaTela(valorTrocoOriginal)
