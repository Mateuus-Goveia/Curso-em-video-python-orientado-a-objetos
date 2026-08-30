"""
Desafio 021

Crie a classe Caneta, que simula o funcionamento de uma caneta colorida,
podendo escrever frases na cor relativa
"""

from rich import print

class Caneta:

    def __init__(self, cor):
        self.cor = cor.lower().strip()
        self.tampa = True


    def destampar(self):
        self.tampa = False
        return self.tampa


    def escrever(self, frase):
        if self.tampa:
            print(f":cross_mark: Caneta tampada !")
        else:
            match self.cor:
                case "verde":
                    print(f"[green]{frase}[/]")
                case "azul":
                    print(f"[blue]{frase}[/]")
                case "vermelho" | "vermelha":
                    print(f"[red]{frase}[/]")
                case _:
                    print("Nao temos essa cor de caneta :loudly_crying_face:")
