soma = cont = 0
while True:
    num = int(input("Digite um número [999 parar]: "))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f"Voce digitou {cont} números e a soma deles é {soma} ")