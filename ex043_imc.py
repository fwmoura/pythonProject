peso = float(input('Qual seu peso? (KG): '))
altura = float(input('Qual sua altura? (m): '))

imc = peso / (altura ** 2)
print('seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso.')
elif 18.5 <=  imc < 25:
    print('Voce está no peso ideal.')
elif 25 <=  imc <30:
    print('Voce está com Sobrepeso.')
elif 30 <=  imc < 40:
    print('Voce está obeso.')
else:
    print('Voce está com obesidade morbida.')
