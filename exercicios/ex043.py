aultura = float(input("Qual sua autura ? "))
peso = float(input("Qual seu peso ? "))
imc = peso / (aultura * aultura)

if imc < 18.5:
    print("Seu IMC é de {:.2f}, você esta abaixo do peso".format(imc))
elif 18.5 <= imc <= 25:
    print("Seu IMC é de {:.2f}, você esta no peso ideal".format(imc))
elif 25 <= imc <= 30:
    print("Seu IMC é de {:.2f}, você esta com sobrepeso".format(imc))
elif 30 <= imc <= 40:
    print("Seu IMC é de {:.2f}, você esta com obesidade".format(imc))
else:
    print("Seu IMC é {:.2f}, vocé esta com obesidade mórbida".format(imc))