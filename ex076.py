listagem = ('Lápis',1.75,"Borracha", 0.30,
"Apontador", 1.10,
"Caderno", 15.0,
"Caneta", 2.50,
"Livros", 40.0)
print("-"*40)
print(f'{"LISTAGEM DE PREÇO":40}')
print("-"*40)
for pos in range (0,len(listagem)):
    if pos % 2== 0:
        print(f"{listagem[pos]:.<30}", end='')
    else:
        print(f"R$ {listagem[pos] :>7.2f}")
print("-"*40)






