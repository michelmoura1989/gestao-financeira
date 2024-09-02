class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.transacoes = []

    def depositar(self, valor, data):
        self.saldo += valor
        self.transacoes.append({'tipo': 'Depósito', 'valor': valor, 'data': data})

    def sacar(self, valor, data):
        if valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append({'tipo': 'Saque', 'valor': -valor, 'data': data})
        else:
            print("Saldo insuficiente")

# Exemplo de uso
conta = Conta("Usuário 1")
conta.depositar(100, "2024-08-23")
conta.sacar(50, "2024-08-24")
print(conta.transacoes)
