quantos_dias = int(input('Quantos dia o carro foi alugado? '))
quantos_km = float(input('Quantos km foram rodados ? '))
converção = (60 * quantos_dias) + (0.15 * quantos_km)
print('O toral a pagar é R${:.2f}'
      .format(converção))