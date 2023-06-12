import math
co = float (input('Digite o cumprimento do cateto oposto '))
ca = float(input('Digite o comprimeto do cateto adjacente'))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

