listado_compras = [
    ["NOMBRE", "GENERO", "COMPRAS"],
    ["Paco", "Hombre", 3],
    ["María", "Mujer", 7],
    ["Susana", "Mujer", 2],
    ["Mario", "Hombre", 10],
    ["Sandra", "Mujer", 1],
    ["Juan", "Hombre", 5],
    ["Mercedes", "Mujer", 4],
    ["Nuria", "Mujer", 2]
]

# 1
del listado_compras[0]

# 2
total_compras_hombre = 0
total_compras_mujer = 0
for fila in listado_compras:
    genero = fila[1]
    compras = fila[2]

    if genero == "Hombre":
        total_compras_hombre += compras
    elif genero == "Mujer":
        total_compras_mujer += compras
    else:
        print("El género de la fila '{}' es erróneo".format(fila))

# 3
if total_compras_hombre > total_compras_mujer:
    print("Las mujeres realizan menos compras que los hombres")

# 4
texto = "Las mujeres compran un total de: {}\n" \
        "Los hombres compran un total de: {}".format(total_compras_mujer,
                                                     total_compras_hombre)
print(texto)
