constante_gravitacional = 6.674 * (10 ** -11)
masa_de_la_tierra = 5.972 * (10 ** 24)
masa_de_la_luna = 7.149 * (10 ** 22)
distancia_tierra_a_luna = 384400 * 1000

parte_arriba_formula = masa_de_la_tierra * masa_de_la_luna
parte_abajo_formula = distancia_tierra_a_luna ** 2

fuerza_de_atraccion = constante_gravitacional * (parte_arriba_formula / parte_abajo_formula)

print(fuerza_de_atraccion)
