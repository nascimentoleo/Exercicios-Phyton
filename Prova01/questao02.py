notasTroco = [50, 20, 10, 5, 2, 1]

def calculaTroco(valorTotal, valorPago):
	if (valorPago > valorTotal):
		troco = abs(valorPago - valorTotal)
		totalDeNotas = []
		for nota in notasTroco:
			while(troco >= nota):
				troco -= nota
				totalDeNotas.append(nota)
		return totalDeNotas

valorTotal = int(input("Digite o valor da conta \n"))
valorPago = int(input("Digite o valor pago \n"))
print("As notas a serem dadas no troco sao " + str(calculaTroco(valorTotal, valorPago)))


