n1 = float(input('nota um:'))
n2 = float(input('nota dois:'))
m = (n1+n2)/2
print('A sua nota foi {:.1f}.'.format(m))
if m >= 6.0:
    print('ótimo trabalho!')
else:
    print('não foi desta vez:{')
    