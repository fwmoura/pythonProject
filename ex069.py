tot18 = toth = totm20 = 0
while True:
    idade = int(input("Idade: "))
    sexo= " "
    while sexo not in "MF":
        sexo = str(input("Sexo: ")).strip() .upper() [0]
        if idade >= 18:
            tot18 += 1
        if sexo == "M":
            toth += 1
        if sexo == "F" and idade < 20:
            totm20 += 1
    
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar?")).strip() .upper() [0]
    if continuar == "N":
        break
print (f"Total de pessoas com mais de 18 {tot18}")
print (f"Total de homens {toth}")
print(f"Total de Mulheres com menos de 20 anos {totm20}")

