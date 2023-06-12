from time import sleep
for c in range(1,999):
    print(f"---> {c}ºimport <---")
    menu = vvenda = lucro = lucroml = vunidade = 0
    
    produto = str(input("Digite qual produto vai importar: "))
    vprod = float(input("Digite o valor unitário do produto (em dolar): "))
    qtproduto= int(input("Digite a quantas unidades voce comprou deste produto: "))
    vdolar = float(input("Qual valor do real x dolar no dia  desta compra? "))
    frete = float(input("Qual valor do frete? (em dolar) "))
    vtaxa = float(input("Em quanto foi taxado? (em reais) "))

    tdolar = (vprod * qtproduto) + frete
    treais = tdolar * vdolar
    vunidade = treais / qtproduto
    
    print(f"total em dolar: {tdolar:.2f}")
    print(f"Total em reais: {treais:.2f}")
    print(f"Compramos {qtproduto:.0f} unidades, e cada uma saiu por {vunidade:.2f} Reais")
    
    print(f"Fim do {c}º Import, Registro realizado com sucesso!")
    
    
    while True:
        print("""
        [1]Lancar nova importação
        [2]Calcular lucro na venda no boca a boca
        [3]Calcular Lucro na venda pelo ML (-30%)
        [0]Sair""")
        menu = int(input("E agora, o que deseja fazer? "))
            
        if menu == 1:
            break
        elif menu == 2:
            vvenda = float(input("Qual valor da venda? "))
            lucro = vvenda - vunidade
            print(f"O Lucro Liquido dasta venda foi {lucro:.2f}")
        elif menu== 3:
            vvenda = float(input("Qual valor da venda? "))
            lucroml = (vvenda - (30*vvenda/100)) - vunidade
            print(f"O Lucro Liquido dasta venda pelo ML foi {lucroml:.2f}")
        elif menu == 0:
            print("Saindo...Até logo!")
            sleep(2)
            print("Fui!!!")
            break
        else:
            print("Opção inválida, verifique novamente as opcoes do menu: ")

    print("__//__"*20 )
