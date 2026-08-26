"""
DESAFIO 017

Crie a classe Produto, onde podemos cadastar nome e o preço.
Crie também um método que mostra uma etiqueta de preço do produto.
"""

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa = Panel(f"{self.nome}\n{self.preco}", title="Produto", width=30)
        return caixa

p1 = Produto("Iphone", 15000)
print(p1.etiqueta())
