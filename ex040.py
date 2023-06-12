nota1 = float(input('Qual a nota da primeira prova? '))
nota2 = float(input('Qual a nota da segunda prova? '))
media = (nota1 + nota2) / 2
print('Sua média foi: {}'.format(media))
if media >= 7:
    print('APROVADO!')
elif media <=5:
    print('REPROVADO!')
else:
    print('RECUPERACAO')
