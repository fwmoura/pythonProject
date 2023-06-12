from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print("Os valores sorteados foram: ")
for n in numeros:
    print(f"{n} ") 
print(f"O maior número sorteado foi {max(numeros)}")
print(f"O menor número sorteado foi {min(numeros)}")