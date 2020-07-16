# 1
tupla1 = ("manzana", "rojo", "dulce")
tupla2 = ("melocotón", "naranja", "ácido")
tupla3 = ("plátano", "amarillo", "amargo")

print(tupla1)

# 2
lista_de_tuplas = []
lista_de_tuplas.append(tupla1)
lista_de_tuplas.append(tupla2)
lista_de_tuplas.append(tupla3)

# 3
for fruta, color, sabor in lista_de_tuplas:
    print("La {fruta} es {color} "
          "y sabe a {sabor}".format(fruta=fruta,
                                    color=color,
                                    sabor=sabor))
