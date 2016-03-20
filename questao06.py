def lerNotas(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite uma nota \n"))
	return m

def lerNotasDeAlunos(limiteMax):
	m = []
	for i in range(0, limiteMax):
		m.append(lerNotas(4))
	return m

def getMediaDeAlunos(alunos):
	medias = []
	for aluno in alunos:
		medias.append(getMedia(aluno))
	return medias

def getMedia(notas):
	totalNotas = 0
	for item in notas:
		totalNotas = totalNotas + int(item)
	return totalNotas / len(notas)

def getAprovados(notas):
	totalAprovados = 0
	for nota in notas:
		if(int(nota) >= 7):
			totalAprovados = totalAprovados + 1
	return totalAprovados

alunos = lerNotasDeAlunos(10)
medias = getMediaDeAlunos(alunos)
aprovados = getAprovados(medias)

print(alunos)
print(medias)
print(aprovados)
