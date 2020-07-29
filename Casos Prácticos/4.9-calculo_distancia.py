# 1
horas = range(1, 11)

# 2
velocidad = 120

# 3
for hora in horas:
    distancia = velocidad * hora
    texto = "A las {hora}:00 el coche ha recorrido {distancia}kms " \
            "a una velocidad de {velocidad}km/h".format(hora=hora,
                                                        distancia=distancia,
                                                        velocidad=velocidad)
    print(texto)
