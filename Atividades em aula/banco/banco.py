class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.historicoSaques = []
        self.historicoDepositos = []
        self.clientes = clientes
        self.número = número
        self.deposito(saldo)
        
    def resumo(self):
        print('CC Número: %s Saldo: %10.2f \n Historico de Saques %s  \n Historico de Depositos %s ' %
                (self.número, self.saldo, self.historicoSaques, self.historicoDepositos))
    
    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historicoSaques.append(valor)

    def deposito(self, valor):
        self.saldo += valor
        self.historicoDepositos.append(valor)

    def getClientes(self):
        result = ""
        for cliente in self.clientes:
            result += cliente.nome + " - " + cliente.telefone
            result += "\n"
        return result

