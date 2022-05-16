#função append() adiciona um elemento a lista
#exemplo lista.append()

aluno1 = []
aluno2 = []

for nota1 in range(3):
    aluno1.append(float(input('Nota:')))

for nota2 in range(3):
    aluno2.append(float(input('Nota:')))

#função sum(), soma todos itens de uma lista
media1 = sum(aluno1)/3
media2 = sum(aluno2)/3
media3 = (media1 + media2)/2
aluno1.append('%.1f' %media1)
aluno2.append('%.1f' %media2)
print('notas aluno1: ', aluno1, '\nnotas aluno2: ', aluno2)
print('media do aluno1: %.1f' %media1)
print('media do aluno2: %.1f' %media2)
print('media entre os dois alunos: %.1f' %media3)