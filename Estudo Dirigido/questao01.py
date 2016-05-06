def ehTriangular(num):
	i = 1 #comeca do 1
	valorMultiplicacao = triangula(i) 
	while (valorMultiplicacao <= num):
		i += 1
		if (valorMultiplicacao == num):
			return True
		valorMultiplicacao = triangula(i)
	return False	

def triangula(valor):
	return valor * (valor + 1) * (valor + 2)

num = int(input("Digite o numero para verificar triangulação \n"))

if (ehTriangular(num)):
	print("É triangular")
else:
	print("Não é triangular")
