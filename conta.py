
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} reais do titular{}".format(self.__saldo, self.titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print ("O valor {} passou do limite. Você tem {} Reais disponíveis.".format(valor, self.__saldo+self.__limite))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
