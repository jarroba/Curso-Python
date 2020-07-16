# 1
texto = "     En Xn lXgar de la mancha, de " \
        "cxyo nombre no qXiero acordarme, " \
        "no ha mXcho tiempo qXe vivía xn " \
        "hidalgo de los de lanza en astillero, " \
        "adarga antigxa, rocín flaco y galgo " \
        "corredor...   "

# 2
texto = texto.strip()

# 3
texto = texto.lower()
texto = texto.replace("x", "u")
print(texto)

# 4
texto = texto.replace(".", "")
texto = texto.replace(",", "")
print(texto)

# 5
lista_de_palabras = texto.split(" ")
lista_de_palabras_ordenadas = sorted(lista_de_palabras)
print(lista_de_palabras_ordenadas)

# 6
for palabra in lista_de_palabras_ordenadas:
    print("{palabra}: {letra}".format(palabra=palabra,
                                      letra=len(palabra)))

# 7
texto_unido = "|".join(lista_de_palabras_ordenadas)
print(texto_unido)
