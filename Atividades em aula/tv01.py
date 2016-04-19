class Televisao:
	def __init__(self):
		self.tamanho = 70
		self.marca = "Semp Toshiba"
		self.ligada = False
		self.canal = 2
		self.canalMinimo = 1
		self.canalMaximo = 10
	
	def __str__(self):
		return "Marca " + self.marca + " - Tamanho " + str(self.tamanho) + " - Canal " + str(self.canal)

	def muda_canal_para_baixo(self):
		if self.canal > self.canalMinimo:
			self.canal -= 1
		else:
			self.canal = self.canalMaximo 
	
	def muda_canal_para_cima(self):
		if self.canal < self.canalMaximo:
			self.canal += 1
		else:
			self.canal = self.canalMinimo

tv = Televisao()
print(tv)
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
print(tv.canal)