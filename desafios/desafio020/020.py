"""
Crie a classe Gamer, onde podemos cadastrar nome, nick e jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.
"""

from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        return self.jogos_favoritos.append(jogo)

    def ficha(self):
        conteudo = f"Nome real: [bold][black on blue] {self.nome} [/]"
        conteudo += f"\nJogos Favoritos:\n"
        for jogo in self.jogos_favoritos:
            conteudo += f":video_game: {jogo}\n"
        painel = Panel(f"{conteudo}", title=f"Jogador <{self.nick}>", width=40)
        print(painel)
        

g1 = Gamer("Matheus Goveia", "Chomp")
g1.add_favoritos("Zelda")
g1.add_favoritos("Mario")
g1.add_favoritos("Mortal Kombat")
g1.ficha()