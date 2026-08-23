class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} anos de idade, está pesando {self.peso}kg e tem {self.altura}m de altura"

g1 = Gafanhoto()
g1.nome = "Matheus"
g1.idade = 31
g1.peso = 84
g1.altura = 1.75

print(g1.mensagem())

print('alo')
