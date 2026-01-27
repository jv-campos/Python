nota1 = float(input('Digite sua primeira nota: '))
nota2 = float (input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média é {}, voçê esta REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {}, voçê esta de RECUPERAÇÃO '.format(media))
elif media >= 7.0:
    print('Sua média é {}, Voçê esta APROVADO'.format(media))
