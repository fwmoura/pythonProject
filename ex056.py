#MEDIA DE IDADE DE TODOS 
#NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TEM MENOS DE 20 ANOS
somadaidade = 0
mediadaidade = 0
maioridadehomem = 0
nomemaisvelho = " "
totmulher20 = 0


for c in range (1,5):
    print(f"_____ {c}ª PESSOA _____")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()
    somadaidade  += idade
    #para testar o nome do homem mais velho
    if c ==1 and sexo== "M":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == "M"and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    #para testar as mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        totmulher20 +=1
        


mediadaidade = somadaidade / 4
print(f"A média de idade do grupo é {mediadaidade} anos.")
print(f"A idade do homem mais velho é {maioridadehomem} e o nome dele é {nomemaisvelho}")
print(f"Neste grupo tem {totmulher20} Mulherescom menos de 20 anos")

