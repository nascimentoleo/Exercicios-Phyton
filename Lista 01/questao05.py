#Questao 5
#Leonardo Pinheiro do Nascimento

def lerNumeros(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite um numero \n"))
	return m

def getPares(numeros):
	pares = []
	for numero in numeros:
		if(int(numero) % 2 == 0):
			pares.append(numero)
	return pares

def getImpares(numeros):
	impares = []
	for numero in numeros:
		if(int(numero) % 2 != 0):
			impares.append(numero)
	return impares
			

numeros = lerNumeros(10)
pares = getPares(numeros)
impares = getImpares(numeros)

print(numeros)
print(pares)
print(impares)

