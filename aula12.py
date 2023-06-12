nome = str(input('Digite seu nome: '))
print('Bom dia, {}!'.format(nome))
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome == 'Joao' or nome == 'Carol' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil')
else:
    print('Que estranho heim?! hahah')
