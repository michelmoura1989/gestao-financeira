class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito: R${valor}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            # Esquece de registrar a transação do saque
        else:
            print("Saldo insuficiente")

# Exemplo de uso
conta = Conta("Usuário 1")
conta.depositar(100)
conta.sacar(50)
print(conta.transacoes)  # Erro: Saque não registrado
