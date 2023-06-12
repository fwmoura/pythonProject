distancia = float(input('Qual a distancia da sua viagem em KM? '))
print('calcularemos o preco da sua viagem de {:.0f}KM.'. format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da passagem para viajar {:.0f}KM é de {:.2f}R$'.format(distancia,preco))
