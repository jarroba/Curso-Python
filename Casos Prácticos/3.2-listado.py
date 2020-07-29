# 1
lista_de_textos = [
    "Coche",
    "Barco",
    "Avión",
    "Bicicleta",
    "Tractor"
]

# 2
del lista_de_textos[2]

# 3
lista_de_textos.append("NUEVO")

# 4
elemento = lista_de_textos.pop(0)
print(elemento)

# 5
longitud = len(lista_de_textos)
print("La lista tiene {}".format(longitud))

# 6
acumulados = ""
for element in lista_de_textos:
    acumulados = acumulados + element
    print(acumulados)
