a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número:'))
# verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O MENOR valor digitado é: {}'.format(menor))
print('O MAIOR valor digitado é: {}'.format(maior))

