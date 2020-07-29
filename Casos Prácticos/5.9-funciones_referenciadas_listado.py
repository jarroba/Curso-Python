# 1
def imprime_mola(contador):
    print("MOLA {}".format(contador))

def imprime_mazo(contador):
    print("mazo {}".format(contador))

# 2
listado_funciones = [imprime_mola,
                     imprime_mazo,
                     imprime_mola,
                     imprime_mazo,
                     imprime_mazo,
                     imprime_mazo]

# 3
for contador, funcion in enumerate(listado_funciones):
    funcion(contador)
