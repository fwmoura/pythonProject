from time import sleep
n1= int(input("Primeiro Valor: "))
n2= int(input("Segundo Valor: "))
opcao = 0
while opcao != 5:
    print("""    [1] SOMAR
    [2]MULTIPLICAR
    [3]MAIOR NUM
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA """)
    opcao = int(input(">>>>Qual é a sua opção? "))

    if opcao == 1:
        soma= n1+n2
        print(f"O resultado da soma é {soma} ")
    elif opcao == 2:
        multiplica= n1*n2
        print(f"O resultado da Multiplicacao é {multiplica} ")
    elif opcao == 3:
        if n1>n2:
            print("O Primeiro número é maior!")
        if n2>n1:
            print("O Segundo número é maior! ")
    elif opcao == 4:
        print("Informe os números novamente:")
        n1= int(input("Primeiro Valor: "))
        n2= int(input("Segundo Valor: "))
    elif opcao == 5:
        print("Finalizando programa ...")
    else:
        print("Opcão inválida, digite novamente: ")
    print("-==-"*20)
    sleep(2)      
print("Fim do programa!")


