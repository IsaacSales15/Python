class Aluno:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def estudar(self, materia):
        print(f"Olá, eu sou {self.nome} e estou estudando {materia}!")
