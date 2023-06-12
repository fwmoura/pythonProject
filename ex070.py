'''A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
total = totmil = menorv = cont = 0
barato = " "
while True:
    produto = str(input("Digite o nome do Produto: "))
    preco = float(input("Digite  o preço do Produto: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menorv:
        menorv = preco
        barato = produto

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip() .upper() [0]
    if continuar == "N":
        break
print(f" O total da sua compra foi R${total:.2f}")
print(f"Total de {totmil} produtos com valor maior de R$1000,00")
print(f"O produto mais barato foi o {barato}, o valor dele é {menorv}")