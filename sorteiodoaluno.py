import random
a1=str(input('digite o nome do aluno 1: '))
a2=str(input('digite o nome do aluno 2: '))
a3=str(input('digite o nome do aluno 3: '))
alunos=[a1,a2,a3]
aluno_sorteado = random.choice(alunos)
print("O aluno sorteado foi:{}".format(aluno_sorteado))