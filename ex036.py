casa = float(input('Qual valor do imóvel que deseja comprar? '))
salario = float(input('Qual sua renda atual?'))
tempo = int(input('Em quantos anos você pretende pagar?'))
parcela = casa/ (tempo*12)
print(('O valor de cada parcela para pagar {:.2f} em {} anos será de {:.2f}'.format(casa,tempo,parcela)))
prestacao = (salario * 30 / 100)
if parcela <= prestacao:
    print('Parabens voce foi aprovado!')
else:
    print('Infelizmente seu emprestimo nao foi aprovado., tente novamente em 3 meses.')