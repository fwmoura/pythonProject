frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes nesta frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}. '.format(frase.find('A')+1))
print('A Ultima letra A apareceu na posição {}.'.format(frase.rfind('A')+1))

print('A letra B apareceu {} vezes nesta frase.'.format(frase.count('B')))
print('A primeira letra B aparece na posição {}. '.format(frase.find('B')+1))
print('A Ultima letra B apareceu na posição {}.'.format(frase.rfind('B')+1))
