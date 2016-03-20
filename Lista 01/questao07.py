#Questao 7
#Leonardo Pinheiro do Nascimento

def lerElementos(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite um elemento \n"))
	return m

def intercala(lista1, lista2, tamanho):
	listaIntercalada = []
	for i in range(0,tamanho):
		listaIntercalada.append(lista1[i])
		listaIntercalada.append(lista2[i])
	return listaIntercalada

lista1 = lerElementos(10)
lista2 = lerElementos(10)
print(intercala(lista1, lista2, 10))