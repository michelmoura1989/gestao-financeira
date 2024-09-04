import tkinter as tk
from tkinter import messagebox

class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.transacoes = []

    def depositar(self, valor, descricao, data):
        self.saldo += valor
        self.transacoes.append({'descricao': descricao, 'valor': valor, 'data': data})
        messagebox.showinfo("Depósito realizado", f'Depósito de R${valor} realizado em {data}: {descricao}')

    def sacar(self, valor, descricao, data):
        if valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append({'descricao': descricao, 'valor': -valor, 'data': data})
            messagebox.showinfo("Saque realizado", f'Saque de R${valor} realizado em {data}: {descricao}')
        else:
            messagebox.showerror("Saldo insuficiente", "Saldo insuficiente para realizar o saque.")

    def saldo_atual(self):
        return self.saldo

    def extrato(self):
        extrato = f'Extrato da conta {self.nome}:\n'
        for transacao in self.transacoes:
            extrato += f'{transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]}\n'
        return extrato

class AplicacaoFinanceira(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão Financeira")
        self.geometry("400x300")

        self.conta = Conta("Empresário XYZ")

        self.label_nome = tk.Label(self, text="Nome da Conta:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(self)
        self.entry_nome.insert(0, self.conta.nome)
        self.entry_nome.pack()

        self.label_saldo = tk.Label(self, text="Saldo Atual:")
        self.label_saldo.pack()

        self.label_valor_saldo = tk.Label(self, text=f'R${self.conta.saldo_atual()}')
        self.label_valor_saldo.pack()

        self.label_operacao = tk.Label(self, text="Operação (Depósito/Saque):")
        self.label_operacao.pack()

        self.entry_operacao = tk.Entry(self)
        self.entry_operacao.pack()

        self.label_valor = tk.Label(self, text="Valor:")
        self.label_valor.pack()

        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack()

        self.label_descricao = tk.Label(self, text="Descrição:")
        self
