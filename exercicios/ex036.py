val_casa = int(input('Qual o valor do seu emprestimo ? '))
salario = int(input('Qual o seu salário ? '))
anos = int(input('Em quantos anos você quer pagar ? '))
prestacao = val_casa / (anos * 12)
minimo = val_casa * 30 / 100

if prestacao <= minimo:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')

print('Para pagar uma casa de {:.2f}, em {} anos. A prestação sera de {:.2f}'.format(val_casa, anos, prestacao))
