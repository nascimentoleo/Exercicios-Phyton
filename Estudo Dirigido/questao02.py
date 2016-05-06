def ehPrimo(num):
	for i in range(2, num - 1):
		if(num % i == 0):
			return False
	return True

num = int(input("Digite o número para saber se é primo \n"))

if (ehPrimo(num)):
	print("É primo")
else:
	print("Não é primo")
