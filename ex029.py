velocidade = float(input("Qual velocidade atual do carro ? "))
if velocidade > 80:
    print('MULTADO! Voce ultrapassou o limite permitido de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar a multa de R${:.2f} por ultrapassar o limite permitido.'.format(multa))
else:
    print('tudo certo, pode prosseguir! ')

