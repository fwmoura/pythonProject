cont = 0
n = int(input('Número: '))
if n <= 10:
    for c in range(1, 11):
        if n % c != 0:
            print(f'\033[31m{c}\033[m', end=' ')
        else:
            print(f'\033[34m{c}', end=' ')
            cont += 1
elif n > 10:
    for c in range(1, n +1):
        if n % c != 0:
            print(f'\033[31m{c}\033[m', end=' ')
        else:
            print(f'\033[31m{c}', end=' ')
            cont += 1
print(f'\nO número {n} foi divisível {cont} vezes.')
if cont == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele NÃO é um número PRIMO!')