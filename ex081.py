valores = []
while True:
    valores.append(int(input("Digite um número: ")))
    resp = str(input("Deseja Continuar? S/N: "))
    if resp in "Nn":
        break
print("-=-"*30)
print(f"Você digitou {len(valores)} números")
print(f"Os numeros incluidos na lista foram {valores}")
valores.sort(reverse=True)
print(f"Os numeros em ordem decrescente {valores}")
if 5 in valores:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O  Valor 5 nao foi encontrado na lista")
