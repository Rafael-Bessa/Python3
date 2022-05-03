class Conta:

    def __init__(self,numero, nome, saldo):
        print("Verificando Construtor, construindo objeto")
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def alterarNome(self, novoNome):
        self.__nome = novoNome
        print(f"O nome da conta agora é {self.__nome}")

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if(valor <= self.__saldo):
            self.__saldo -= valor
            print(f"Você sacou R$ {valor} e sobrou R$ {self.__saldo}")
        else:
            print("Você não tem saldo para fazer este saque")

    def extrato(self):
        print(f"Seu extrato é de {self.__saldo}")

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo