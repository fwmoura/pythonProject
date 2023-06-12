from random import randint
v=0
while True:
    jogador = int(input("Digite um número de 0 a 10: "))
    computador = randint(0,11)
    total= jogador + computador
    jogada= " "
    while jogada not in "PI":
            jogada = str(input("escolha se quer PAR ou ÍMPAR [P/I]:")).upper().strip()
    print(f"Você jogou {jogador} e o computador jogou {computador} o total é {total}")
    if jogada == "P":
        if total %2 ==0:
            print("Deu PAR você venceu!")
            v+=1
        else:
            print("deu IMPAR Você perdeu!!")
            break
    elif jogada == "I":
        if total %2 == 1:
            print("deu IMPAR Você venceu!")
            v+=1
        else:
            print("Deu PAR você perdeu!")
            break
    print("Vamos Jogar Novamente...")
print(f"GAME OVER!! você venceu {v} Rodadas")       
    
