salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    aumento = salario + (salario * 0.1)
else: 
    aumento = salario + (salario * 0.15)

print('Seu salário de R${:.2f} agora é R${:.2f}'.format(salario, aumento))