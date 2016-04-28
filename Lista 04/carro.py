class Carro:
	def __init__(self, consumo):
		self.consumo = consumo
		self.combustivel = 0

	def mover(self, distancia):
		if(self.combustivel > 0):
			self.combustivel -= distancia / self.consumo

	def gasolina(self):
		return self.combustivel

	def abastecer(self, litros):
		self.combustivel += litros





