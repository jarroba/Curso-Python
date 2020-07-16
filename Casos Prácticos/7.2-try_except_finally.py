numeros = ["100", "200", "300", "cuatrocientos", "500"]

for numero_str in numeros:
    try:
        numero = int(numero_str)
    except ValueError:
        print("'{}' no se puede convertir a "
              "entero".format(numero_str))
        numero = None
        break
    finally:
        print("Entero: {}".format(numero))
    print("Fin iteración")
print("Termia el bucle")
