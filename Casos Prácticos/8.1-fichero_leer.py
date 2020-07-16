ruta_hasta_fichero = "ruta/mi_fichero.txt"

# 1
with open(ruta_hasta_fichero, "r") as fichero:
    for linea in fichero.readlines():
        # 2
        print(linea.strip())
