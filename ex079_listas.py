numero = list()
while True:
    n = int(input("digite um numero: "))
    if n not in numero:
        numero.append(n)
        print("Numero adiciodado com sucesso!")
    else:
        print("Valor já existente na lista")
    r = str(input("Deseja continuar? S/N "))
    if r in "Nn":
        break
print("_*"*30)
numero.sort()
print(f"A lista ficou assim: {numero}")

# numero = list()
# while True:
#     n = int(input("Digite um número: "))
#     numero.append(n)
#     if n == 0:
#         break
# print(f"A lista ficou assim {numero}")