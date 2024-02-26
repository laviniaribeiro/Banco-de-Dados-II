class Professor:
    def __init__(professor, nome):
        professor.nome = nome

    def ministrar_aula(professor, assunto):
        print(f'O professor {professor.nome} está ministrando uma aula sobre {assunto}.')

frederico = Professor('Frederico')
frederico.ministrar_aula('Banco de dados') 

class Aluno:
    def __init__(aluno, nome):
        aluno.nome = nome

    def presenca(aluno):
        print(f'O aluno {aluno.nome} está presente.')

joão = Aluno('João')
joão.presenca()
maria = Aluno('Maria')
maria.presenca()
joaquim = Aluno('Joaquim')
joaquim.presenca()
fifi = Aluno("Fifi")
fifi.presenca()

class Aula:
    def __init__(aula, professor, assunto):
        aula.professor = professor
        aula.assunto = assunto
        aula.alunos = []

    def adicionar_aluno(aula):
        aula.alunos.append(Aluno)
    
    def listar_presenca(aula):
        print(f'Presença na aula sobre {aula.assunto}, ministrada pelo {aula.professor}: ')
        for aluno in aula.alunos:
            aluno.presenca()

aula = Aula('frederico', 'Banco de dados')
aula.adicionar_aluno(joão)
aula.adicionar_aluno(maria)
aula.adicionar_aluno(joaquim)
aula.adicionar_aluno(fifi)
print(aula.listar_presenca())


