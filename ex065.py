resp = "S"
soma = cont = media = menor = maior =  0
while resp != "N":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
media = soma / cont
print(f"Voce digitou {cont} números, e a média deles foi {media :.2f}")
print(f"O maior valor digitado foi {maior} , e o menor valor digitado foi {menor}")
    