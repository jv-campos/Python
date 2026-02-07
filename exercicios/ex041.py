import datetime
ano = int(input("Qual o ano em que você nasceu ? "))
atual = datetime.day().year
idade = atual - ano


if idade <= 9:
    print("Categoria: MIRIM")
elif idade <=14:
    print("Categpria: INFANTIL")
elif idade <= 19:
    print("Categpria: JUNIOR")
elif idade <= 25:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")