# 1
listado_para_guardar = [
    "línea 1",
    "línea 2",
    "línea 3"
]

ruta = "ruta/fichero.txt"

with open(ruta, "w") as fichero:
    for linea in listado_para_guardar:
        fichero.write("{}\n".format(linea))

# 2
listado_para_sobrescribir = [
    "línea sobrescrita 1",
    "línea sobrescrita 2",
    "línea sobrescrita 3",
]
with open(ruta, "w") as fichero:
    for linea in listado_para_sobrescribir:
        fichero.write("{}\n".format(linea))


# 3
listado_para_aniadir = [
    "línea 4",
    "línea 5"
]
with open(ruta, "a") as fichero:
    for linea in listado_para_aniadir:
        fichero.write("{}\n".format(linea))
