"""
DESAFIO 019

Crie a classe Livro, que vai simular a passagem de paginas de um livro,
considerando tambem se o usuario chegou ao fim da leitura.
"""

from rich import print
from time import sleep


class Livro:

    def __init__(self, paginas: int, nome="Livro"):
        self.nome = nome
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Voce acabou de abrir o livro [red]{self.nome}[/] que tem {self.total_paginas} paginas no total. Voce agora esta na pagina 1")

    def avancar_paginas(self, paginas):
        cont_paginas = 0
        for _ in range(paginas):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                cont_paginas += 1
                print(f"Pag{self.pagina_atual} :right_arrow:  ", end="")
                sleep(0.4)
        print(f"Voce avançou {cont_paginas} paginas e agora esta na pagina {self.pagina_atual}")          


    def fim_do_livro(self):
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro(20, "Arroz com mel")
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
