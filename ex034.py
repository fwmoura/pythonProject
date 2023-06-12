salario = float(input('Digite seu salário atual para saber quanto ficara com o aumento: R$ '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 /100)
print('O salário que era R${:.2f}, com aumento ficará: R${:.2f}'.format(salario,novo))
