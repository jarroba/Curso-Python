# 1
def espacio(velocidad, tiempo):
    resultado = velocidad * tiempo
    # 2
    if resultado < 0:
        return None
    else:
        return resultado

# 3
tiempo_retornado = espacio(120, -10)
print(tiempo_retornado)
