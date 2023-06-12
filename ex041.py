from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Voce tem {} anos, está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('voce tem {} anos, está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('voce tem {} anos, está na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos, está na categoria SENIOR'.format(idade))
else:
    print('Voce tem {} anos, está na categoria MASTER'. format(idade))
