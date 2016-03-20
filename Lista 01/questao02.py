#Questao 2
#Leonardo Pinheiro do Nascimento

def lerInteiro(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite um numero \n"))
	return m

def imprimeInverso():
	print(lerInteiro(10)[::-1])

imprimeInverso()