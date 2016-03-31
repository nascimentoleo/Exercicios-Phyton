nomeDoArquivo = input("Digite o nome do Arquivo \n")

qtdLinhas = qtdPalavras = qtdCaracteres = 0
with open(nomeDoArquivo) as arquivo:
	for linha in arquivo.readlines():
		qtdLinhas += 1
		qtdPalavras += len(linha.split())
		qtdCaracteres += len(linha)

print("Linhas : %d | Palavras : %d | Caracteres : %d" %(qtdLinhas, qtdPalavras, qtdCaracteres))


