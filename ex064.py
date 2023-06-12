n=0
cont = -1 # para nao contar o 999 parar
soma = -999 # para nao somar o 999 parar

while n != 999:
    n = int(input("Digite um numero [999 para parar]: "))
    soma += n
    cont += 1
print(f"voce digitou {cont} números, e a soma deles é {soma}")
