# 1
secuencia = "Texto"

# 2
letra_anterior = None

# 3
for letra in secuencia:
    print("Letra actual '{char}' y letra anterior "
          "'{char_prev}'".format(char=letra,
                                 char_prev=letra_anterior))
    letra_anterior = letra
