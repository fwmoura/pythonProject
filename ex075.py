num = (int(input("Digite um numero: ")),
int(input("Digite outro numero: ")),
int(input("Digite mais um numero: ")),
int(input("Digite ultimo numero: ")),)

print(f"Os números digitados foram {num}")
print(f"O número nove apareceu {num.count (9)} vezes")
if 3 in num:
    print(f"O número 3 apareceu na {num.index(3)+1}ª posicao")
else:
    print("O valor 3 nao foi digitado")
print("Os valores pares digitados foram:")
for n in num:
    if n % 2 == 0:
        print(n)