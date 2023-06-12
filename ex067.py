while True:
    n = int(input("Quer saber a tabuada de qual numero? [DIGITE [0]PARA SAIR] "))
    if n == 0:
        break
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
print("FIM DO PROGRAMA DE TABUADA")
