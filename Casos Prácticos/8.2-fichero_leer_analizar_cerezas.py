ruta_hasta_fichero = "ruta/recogida_cerezas.txt"

with open(ruta_hasta_fichero, "r") as fichero:
    cantidad_total = 0
    linea = fichero.readline()
    while linea:
        linea = linea.strip()

        fecha, cantidad = tuple(linea.split(","))

        try:
            cantidad_total += int(cantidad)
        except ValueError:
            print("linea erronea: {}".format(linea))

        linea = fichero.readline()

print("Cantidad de cerezas totales : {}".format(cantidad_total))
