cont = ('zero','um','dois','tres')
resp= "S" 
while True:
    num = int(input("Digite um número entre zero e tres: "))
    if 0 <= num <= 3:
        break
    print("Tente novamente")  
print(f"Voce digitou o numero {cont[num]}")
