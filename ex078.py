listanum = []
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print("*-*"*30)
print(f"Os Valores digitados foram {listanum}")

print(f"O maior valor digitado foi {mai} na posicao ", end=" ")
for i,v in enumerate (listanum):
    if v == mai:
        print(f"{i}", end= " ")

print(f"O menor valor digitado foi {men} na posicao ", end=" ")
for i,v in enumerate(listanum):
    if v == men:
        print(f"{i}", end= " ")

