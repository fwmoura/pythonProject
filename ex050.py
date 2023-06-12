somap = 0
somai = 0
cont = 0
conti = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        somap = somap + num
        cont = cont + 1
    elif num % 2 != 0:
        somai = somai + num
        conti = conti + 1
print(f'Voce informou {cont} números pares e a soma foi {somap}')
print(f"Informou também {conti} números impares e a soma foi {somai}")

