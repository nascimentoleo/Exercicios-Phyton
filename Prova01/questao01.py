def ondeAparece(frase, caracter = 'a'):
	posicoes = []
	for i in range(0, len(frase)):
		if (frase[i] == caracter):
			posicoes.append(i)
	return posicoes

primeiraFrase = "Esta e a primeira frase"
segundaFrase  = "Esta e a segunda frase"
terceiraFrase = "Esta e a terceira frase"

listaDeOcorrencias = []

listaDeOcorrencias.append(ondeAparece(primeiraFrase, 'e'))
listaDeOcorrencias.append(ondeAparece(segundaFrase, 's'))
listaDeOcorrencias.append(ondeAparece(terceiraFrase))

print(listaDeOcorrencias)




