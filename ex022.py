nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seus dados...')
print('seu nome em letras maiúsculas é: {} '.format(nome.upper()))
print('seu nome em letras minúscula é: {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

