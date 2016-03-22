def ehPrimo(numero):
	divisores = 0
	for i in range(1, numero):
		if(numero % i == 0):
			divisores = divisores + 1
	if(divisores >= 2):
		return False
	return True

for i in range(1, 100):
	if(ehPrimo(i)):
		print(str(i) + " é primo")
	else:
		print(str(i) + " não é primo")
