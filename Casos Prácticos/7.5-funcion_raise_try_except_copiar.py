# 1
def escribir_en_la_pizarra(veces):
    # 2
    if veces <= 0:
        raise ValueError("El número tiene que ser 1 o mayor")

    for num in range(1, veces+1):
        print("No copiaré en los exámenes {}".format(num))

# 3
try:
    escribir_en_la_pizarra(10)
except ValueError as mi_error:
    print(mi_error)
