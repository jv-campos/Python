from math import radians, sin, cos, tan

angulo = float(input('Qual o âgulo desejado: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'
      .format(angulo, seno))

cos = cos(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'
      .format(angulo, cos))

tan = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'
      .format(angulo, tan))