import uuid
#unique universal identifier
class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return (f"Matricula: {self.matricula} \n"
                f"Nome: {self.nome} \n"
                f"idade: {self.idade} \n"
                f"curso: {self.curso} \n"
                f"nota: {self.nota} \n")

if __name__ == "__main__":
    aluno = Aluno("Carlos", 32, "Python", 9)
    print(aluno)

