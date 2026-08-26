"""
DESAFIO 018

Crie a classe Churrasco, onde seja possível informar quantas pessoas vao participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

CONSIDERE:
Consumo padrao: 400g por pessoa
Preço: R$82,40/kg
"""

from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self, nome, quantidade: float):
        self.nome = nome
        self.quantidade = quantidade

    def analisar(self):
        qtd_por_pessoa = 0.4
        preco_kg = 82.40
        total_carne = self.quantidade * qtd_por_pessoa
        custo_total = total_carne * preco_kg
        custo_pessoa = custo_total / self.quantidade

        caixa = Panel(
            f"""Analisando [green]{self.nome}[/] com [blue]{self.quantidade} convidados[/]
Cada participante comerá {qtd_por_pessoa}kg e cada Kg custa R${preco_kg:.2f}
Recomendo [blue]comprar {total_carne}kg de carne[/]
O custo total será de [green]R${custo_total:.2f}[/]
Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/] para participar""",
            title=self.nome,
            width=60,
        )

        return caixa


c1 = Churrasco("Churras dos amigos", 15)
print(c1.analisar())
