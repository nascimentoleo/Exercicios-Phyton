def lerNotas(limiteMax):
	m = []
	for i in range(0,limiteMax):
		m.append(input("Digite uma nota \n"))
	return m

def getMedia(notas):
	totalNotas = 0
	for item in notas:
		totalNotas = totalNotas + int(item)
	return totalNotas / len(notas)

notas = lerNotas(4)
print(notas)
print("Media " + str(getMedia(notas)))

