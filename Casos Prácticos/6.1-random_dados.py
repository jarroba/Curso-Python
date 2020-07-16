from random import choice

# 1
caras = [1, 2, 3, 4, 5, 6]

dado_uno = choice(caras)
dado_dos = choice(caras)

# 2
suma = dado_uno + dado_dos

# 3
es_impar = suma % 2
if es_impar:
    informacion = "Es impar"
else:
    informacion = "Es par"

print("==Resultados==\n"
      "Primer dado: {uno}\n"
      "Segundo dado: {dos}\n"
      "Suma dados: {suma}\n"
      "{info}".format(uno=dado_uno,
                      dos=dado_dos,
                      suma=suma,
                      info=informacion))
