from collections import Counter

listaDePalavras = []
nomeDoArquivo = input("Digite o nome do Arquivo \n")

with open(nomeDoArquivo) as arquivo:
	for linha in arquivo.readlines():
		for palavra in linha.split():
			listaDePalavras.append(palavra)
ocorrencias = Counter(listaDePalavras)			
print(ocorrencias)
