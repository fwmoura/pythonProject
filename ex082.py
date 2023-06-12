valores = []
pares = []
impares = []
while True:
    valores.append(int(input("Digite um numero: ")))
    resp = str(input("Deseja Continuar? S/N "))
    if resp in "Nn":
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
    
print(f"A lista completa {valores}")
print(f"Os Pares {pares}")
print(f"Os Impares{impares}")
