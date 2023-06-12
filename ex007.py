nome=input('Nome?')
materia = input('Matéria?')
p1 = float(input('quanto o aluno tirou na prova 1?'))
p2 = float(input('quanto o aluno tirou na prova 2?'))
p3 = float(input('quanto o aluno tirou na prova 3?'))
m = (p1+p2+p3)/3
print('{}, sua média em {} é:{}'.format(nome,materia,m))