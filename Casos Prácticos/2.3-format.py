# 1
nombre = "Mario"
apellido = "Bross"
numero = "doce"

# 2
nombre_apellido = nombre + " " + apellido

# 3
texto_format = "{heroe} ha subido " \
               "al nivel {nivel}".format(heroe=nombre_apellido,
                                         nivel=numero)
print(texto_format)
