def perguntar(pergunta):
	resposta = input(pergunta + " (s)Sim (n)Nao \n")
	if(resposta != "s" and resposta != "n"):
		return perguntar(pergunta)
	return resposta

def julgamento(respostas):
	qtdSim = respostas.count("s")
	if(qtdSim == 2):
		return "Suspeita"
	elif(qtdSim > 2 and qtdSim < 4):
		return "Cumplice"
	elif(qtdSim == 5):
		return "Assassino"
	else:
		return "Inocente"

respostas = []
respostas.append(perguntar("Telefonou para a vitima ?"))
respostas.append(perguntar("Esteve no local do crime ?"))
respostas.append(perguntar("Mora perto da vitima ?"))
respostas.append(perguntar("Devia para a vitima ?"))
respostas.append(perguntar("Ja trabalhou com a vitima ?"))
print(julgamento(respostas))