# 1
helados = [
    "     chocolate,grande    ",
    "vainilla,pequeño     ",
    "       fresa,mediano",
    "   nata,grande   "
]


def limpiar_y_separar(linea):
    limpia = linea.strip()
    lista_valores = limpia.split(",")
    return lista_valores[0], lista_valores[1]


# 2
helados_grandes = 0
for linea_helado in helados:
    sabor, tamanio = limpiar_y_separar(linea_helado)

    # 3
    print("Calculando tamaño '{}' de sabor '{}'".format(tamanio, sabor))

    if tamanio == "grande":
        helados_grandes += 1

print("Hay {} helados grandes".format(helados_grandes))
