def lerInteiro():
	m = []
	for i in range(0,5):
		m.append(input("Digite um numero \n"))
	return m

def mostraNumeros():
	listaNumeros = lerInteiro()
	for item in listaNumeros:
		print(item)

mostraNumeros()		

