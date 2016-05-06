def fatorar(num):
  fator = 2
  while num > 1:
    multiplicidade = 0
    while num % fator  == 0:
      multiplicidade += 1
      num = num / fator 
    if (multiplicidade != 0):
      print("Fator : %d  Multiplicidade: %d" %(fator , multiplicidade))
    fator  += 1

num = int(input("Digite o número para fatorar \n"))
fatorar(num)

