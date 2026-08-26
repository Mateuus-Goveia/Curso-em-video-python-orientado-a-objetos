"""
DESAFIO 016

Crie a classe Funcionario, onde podemos cadastrar nome, setor,
e cargo. Crie também um método que permita ao funcionário se apresentar.
"""
from rich import print


class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, Sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor}"

f1 = Funcionario("Matheus", "TI", "Programador")
print(f1.apresentacao())
