"""
DESAFIO 019

Crie a classe Livro, que vai simular a passagem de paginas de um livro,
considerando tambem se o usuario chegou ao fim da leitura.
"""

from rich import print
from time import sleep

class Livro:

    def __init__(self, paginas, nome):
        self.total_paginas = paginas
        self.nome = nome
        self.pagina_atual = 1

        print(f":open_book: [blue]Voce acabou de abrir o livro '[red]{self.nome}[/]' que tem [green]{self.total_paginas} paginas[/] no total. Voce agora está na [yellow]página {self.pagina_atual}")

    def avancar_paginas(self, quantidade):
        cont_paginas = 0
        for _ in range(quantidade):
            if not self.verificar_fim_do_livro():            
                self.pagina_atual += 1
                cont_paginas += 1
                print(f":backhand_index_pointing_right: Pag{self.pagina_atual} ", end="")
                sleep(0.4)
        print(f"[blue]Voce acabou de passar {cont_paginas} paginas e agora está na [/][yellow]pagina {self.pagina_atual}[/]")
        if self.verificar_fim_do_livro():
            print(f"Parabens !! voce chegou ao final do livro '[red]{self.nome}[/]'")

    def verificar_fim_do_livro(self):
        return True if self.total_paginas == self.pagina_atual else False

    
l1 = Livro(10, "Livro")
l1.avancar_paginas(50)
