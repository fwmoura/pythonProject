varInput = 99;
while(varInput != 0):
    print('''
[0]SAIR
[1]SOMA
[2]SUBTRACAO
[3]MULTIPLICACAO
[4]DIVISAO''');

    varInput = int(input("Escolha  a operacao: "));
    if varInput == 0:
        break;
    varValue1 = float(input("Primeiro valor: "));
    varValue2= float(input("Segundo valor: "));

    if varInput ==  1:
        print("O resultado da soma é: " + str(varValue1 + varValue2));
    elif varInput ==  2:
        print("O resultado da subtracao é: " + str(varValue1 - varValue2));
    elif varInput ==  3:
        print("O resultado da mutiplicao é: " + str(varValue1 * varValue2));
    elif varInput ==  4:
        print("O resultado da divisao é: " + str(varValue1 / varValue2));
    print("="*80)
