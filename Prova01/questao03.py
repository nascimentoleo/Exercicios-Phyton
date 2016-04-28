def valorPagamento(valorDaPrestacao, numDeDias):
	if(valorDaPrestacao > 0):
		if(numDeDias > 0):
			valorDaPrestacao += valorDaPrestacao * 0.03
			valorDaPrestacao += valorDaPrestacao * (0.001 * numDeDias)
	return valorDaPrestacao

valorDaPrestacao = -1
relatorio = []

while(True):
	valorDaPrestacao = float(input("Digite o valor da prestacao \n"))
	if (valorDaPrestacao == 0):
		break
	numDeDias = int(input("Digite o numero de dias em atraso \n"))
	valorPago = valorPagamento(valorDaPrestacao, numDeDias)
	print("Valor a ser pago: R$ %.2f" %(valorPago))
	relatorio.append(valorPago)

print("Relatorio de prestacoes a serem pagas: \n ")
for item in relatorio:
	print("%.2f" %(item))
 