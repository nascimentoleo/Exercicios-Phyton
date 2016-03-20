#Questao 4
#Leonardo Pinheiro do Nascimento

def lerLetras(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite uma letra \n"))
	return m

def getConsoantes(expressao):
	vogais = ['a','e','i','o','u']
	consoantes = []
	for letra in expressao:
		if(letra not in vogais):
			consoantes.append(letra)
	return consoantes

expressao = getConsoantes(lerLetras(10))
print(expressao)
print("Quantidade de consoantes " + str(len(expressao)))




