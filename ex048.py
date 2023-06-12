soma = cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        cont += 1
        soma += c
        #print (c, end= " ")
print(f"A soma de todos os {cont} numeros digitados é {soma}")