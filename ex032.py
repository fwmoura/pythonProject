from datetime import date
ano = int(input('Que ano quer analisar? Para analisar o ano atual basta digitar 0:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} nao é BISSEXTO'.format(ano))
