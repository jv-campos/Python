f20 = 0 
m = 0
p18 = 0

print('Bem Vindo. Faça seu cadastro aqui')
while True:
    print('-'*15)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        p18 += 1 
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        f20 += 1 
    resposta = ' ' 
    while resposta not in 'SN':
        resposta = str(input('Quer cadastrar mais alguém ? ')).strip().upper()[0]
    if resposta == 'N':
            break
    print('-'*15)
print(f'Total de pessoas com mais de 18 anos: {p18}\nAo todo temos {m} homen cadastrados\nE temos {f20} mulhere com menos de 20 anos')