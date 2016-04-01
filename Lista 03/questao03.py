def lerUsuarios(nomeDoArquivo):
	with open(nomeDoArquivo) as arquivoDeUsuarios:
		usuarios = {}
		for linha in arquivoDeUsuarios.readlines():
			nomeDeUsuario = linha[0:15].strip() #Pego da posicao 0 a 15
			espacoUtilizado = linha[16:len(linha)].strip() # da posicao 16 ate o fim do arquivo
			usuarios[str(nomeDeUsuario)] = espacoUtilizado 
		return usuarios

def criarRelatorio(usuarios):
	arquivoRelatorio = open("relatório.txt", 'w')
	arquivoRelatorio.write(getCabecalhoDoRelatorio())
	totalDeUsuarios = 1
	espacoTotal = getValorTotal(usuarios.values())
	for key in sorted(usuarios.keys()):
		nomeDoUsuario = key
		espacoUtilizado = byteToMegaByte(float(usuarios[key]))
		arquivoRelatorio.write(getLinha(totalDeUsuarios, nomeDoUsuario, espacoUtilizado, espacoTotal))
		totalDeUsuarios += 1
	arquivoRelatorio.write(getRodapeDoRelatorio(espacoTotal, totalDeUsuarios))

def getValorTotal(totais):
	espacoTotal = 0
	for value in totais:
		espacoTotal += byteToMegaByte(float(value))
	return espacoTotal

def getPorcentagem(espacoUtilizado, espacoTotal):
	return "{:.2f}".format((espacoUtilizado * 100) / espacoTotal)

def byteToMegaByte(valor):
	return (valor /1024) / 1024

def getCabecalhoDoRelatorio():
		return ("ACME Inc. 		     Uso do espaco em disco pelos usuários\n" +
			    "--------------------------------------------------------------------------------- \n" + 
			    "Nr.  Usuário            Espaço utilizado      % do uso\n\n")	

def getRodapeDoRelatorio(espacoTotal, qtdPessoas):
	media = "{:.2f}".format(espacoTotal/qtdPessoas)
	total = "{:.2f}".format(espacoTotal)
	return ("\nEspaço total ocupado:   " + total.ljust(8) + " MB\n" +
		    "Espaço médio ocupado:   " + media.ljust(8) + " MB")

def getLinha(numLinha, nomeDoUsuario, espacoUtilizado, espacoTotal):
	return (str(numLinha) + "    "+  nomeDoUsuario.ljust(20) + 
			"{:.2f}".format(espacoUtilizado).ljust(7) + " MB            " +
			getPorcentagem(espacoUtilizado, espacoTotal).ljust(6) + "%\n")

usuarios = lerUsuarios("usuarios.txt")

criarRelatorio(usuarios)





