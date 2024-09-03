import tkinter as tk

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

def depositar():
    valor = float(entry_valor.get())
    conta.depositar(valor, "2024-08-23")
    label_saldo.config(text=f'Saldo: R${conta.saldo}')  # Erro: saldo não atualiza

conta = Conta("Usuário 1")

root = tk.Tk()
root.title("Conta Bancária")

label_saldo = tk.Label(root, text=f'Saldo: R${conta.saldo}')
label_saldo.pack()

entry_valor = tk.Entry(root)
entry_valor.pack()

btn_depositar = tk.Button(root, text="Depositar", command=depositar)
btn_depositar.pack()

root.mainloop()
