equipo = {
    "capitan": 7,
    "delantero": 8,
    "portero": 2,
    "defensa": 5,
    "centrocampista": 4,
    "entrenador": 1
}

while "capitan" in equipo:
    print("Jugamos un partido con: {}".format(equipo))
    clave_eliminar = input("Eliminamos a:")
    if clave_eliminar in equipo:
        del equipo[clave_eliminar]
    else:
        print("No se ha eliminado a nadie")

print("No jugamos sin capitan")
