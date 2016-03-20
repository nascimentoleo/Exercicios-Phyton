meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def lerTemperatura(meses):
	m = []
	for i in range(0,len(meses)):
		m.append(input("Digite a temperatura do mes " + meses[i] + "\n"))
	return m

def getMedia(valores):
	total = 0
	for item in valores:
		total = total + int(item)
	return total / len(valores)

def getMesesAcimaDaMedia(mediasMeses, mediaAnual, meses):
	mesesAcima = []
	i = 0
	for media in mediasMeses:
		if(int(media) > mediaAnual):
			mesesAcima.append(str(i) + " - " + meses[i])
		i = i + 1
	return mesesAcima

valorMeses = lerTemperatura(meses)
mediaAnual = int(getMedia(valorMeses))
print(getMesesAcimaDaMedia(valorMeses,mediaAnual, meses))