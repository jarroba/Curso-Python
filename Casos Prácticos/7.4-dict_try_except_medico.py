medicos_y_sus_especialidades = {}

continuar = True
while continuar:
    nombre_clave = input("Inserta un médico:")

    if nombre_clave == "salir":
        break

    especialidad_valor = input("Inserta su especialidad:")

    try:
        especialidades = medicos_y_sus_especialidades[nombre_clave]
        especialidades.append(especialidad_valor)
    except KeyError:
        especialidades = [especialidad_valor]

    # try ... except se puede reemplazar por:
    #
    # if nombre_clave in medicos_y_sus_especialidades:
    #     especialidades = medicos_y_sus_especialidades[nombre_clave]
    # else:
    #     especialidades = []
    # especialidades.append(especialidad_valor)

    medicos_y_sus_especialidades[nombre_clave] = especialidades
    print(medicos_y_sus_especialidades)
print("Salir del programa")
