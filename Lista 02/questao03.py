def calculaDimensao(listaDeComprimentos):
	dimensoes = []
	valorDimensao = 0
	for item in listaDeComprimentos:
		valorDimensao = 0
		if(isinstance(item, list)):
			for dimensao in item:
				valorDimensao = valorDimensao + float(dimensao)
			dimensoes.append(valorDimensao)
	return dimensoes

dimensoes = calculaDimensao([[2, 3, 4], [5, 6, 7, 8], [9, 10]])
print(dimensoes)
