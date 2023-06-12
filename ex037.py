num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases de concersao:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMALL''')
opcao = int (input('Sua opcao:'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {2:}'.format(num,bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {2:}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {2:}'.format(num, oct(num)))
else:
    print('Opcao inválida!')
