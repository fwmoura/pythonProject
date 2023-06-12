contsex= 0
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MF":
    sexo= str(input("Dados inválidos, informe seu sexo, M ou F ")).strip().upper()[0]
if sexo == "M":
    contsex +=1
print(f"Sexo {sexo} registrado com sucesso!")
print(f"total de sexo masculino é: {contsex}")