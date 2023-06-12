dias = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
km = float(input('Digite quantos km foram rodados: '))

print(f'O total a pagar é de {60 * dias + 0.15 * km:.2f}')