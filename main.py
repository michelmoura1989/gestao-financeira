class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Exemplo de uso
conta = Conta("Usuário 1")
conta.depositar(100)
print(conta.saldo)
