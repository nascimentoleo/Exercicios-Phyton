def inverteNumero(num):
	return ' '.join([algarismo[::-1] for algarismo in str(num).split()])

print(inverteNumero(1223))