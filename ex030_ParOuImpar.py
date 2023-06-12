num = int(input('Digite um númrero qualquer para dercobrir se ele é PAR ou ÍMPAR: '))
res = num%2
if res == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))
