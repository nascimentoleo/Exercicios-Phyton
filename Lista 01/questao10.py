#Questao 10
#Leonardo Pinheiro do Nascimento
def lerNotas():
	nota = 0
	m = []
	while (True):
		nota = input("Digite uma nota \n")
		if(int(nota) == -1):
			break
		m.append(nota)
	return m

def imprimeValoresInverso(valores):
	for i in range(len(valores) -1, -1 , -1):
		print(valores[i])

def somaDosValores(valores):
	total = 0
	for valor in valores:
		total = total + int(valor)
	return total

def getMedia(notas):
	totalNotas = 0
	for item in notas:
		totalNotas = totalNotas + int(item)
	return totalNotas / len(notas)

def getAcimaDaMedia(valores, media):
	acima = []
	for valor in valores:
		if(int(valor) > media):
			acima.append(valor)
	return acima

def getReprovados(notas):
	totalReprovados = 0
	for nota in notas:
		if(int(nota) < 7):
			totalReprovados = totalReprovados + 1
	return totalReprovados

valores = lerNotas()


print(len(valores))
if (len(valores) > 0):
	imprimeValoresInverso(valores)
	print(somaDosValores(valores))
	media = getMedia(valores)
	print(media)
	print(getAcimaDaMedia(valores, media))
	print(getReprovados(valores))
print("Winter is coming")