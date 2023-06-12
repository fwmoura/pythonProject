n1 = (int(input('Digite um numero inteiro: ')))
n2 = (int(input('Digite outro numero inteiro: ')))
if n1 > n2:
    print('O primeiro Valor é maior!')
elif n2 > n1:
    print("O segundo valor é maior!")
elif n1 == n2 or n2 == n1:
    print("Nao existe valor maior, os dois sao iguais!")
