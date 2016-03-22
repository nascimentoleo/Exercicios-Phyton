def inverteFrase(frase):
	return ' '.join([word[::-1] for word in frase.split()])

print(inverteFrase("Eu gosto de python"))