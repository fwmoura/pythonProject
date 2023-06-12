preco = float(input('Qual vador da sua compra? R$'))
print('''Formas de pagamento
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] a vista no cartao de credito
[ 3 ] ATÉ 2X NO CARTAO
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Escolha uma opcao de pagamento:'))
if opcao == 1:
    desc = preco - (preco * 10 / 100)
    print('a compra paga no dinheiro/cheque tera 10% de desconto e o valor final de {:.2f}R$'. format(desc))
elif opcao == 2:
    desc = preco - (preco * 5 / 100)
    print('Sua compra paga avista no cartao tem 5% de desconto e ficará no valor de {:.2f}R$'.format(desc))
elif opcao == 3:
    parcela = preco/2
    print('Para pagamentos em até 2x no cartao o valor permanece o mesmo: {:.2f}R$ e cada parcela será de {:.2f}R$'.format(preco,parcela))
elif opcao == 4:
    parc = int(input('Digite a quantidade de parcelas que voce deseja: '))
    desc = preco + (preco * 20 / 100)
    juro = desc / parc
    print('O valor total da sua compra parcelada em {}x será {:.2f} , cada parcela no valor de {:.2f}'.format(parc,desc,juro))
else:
    print('OPCAO INVÁLIDA')
    
