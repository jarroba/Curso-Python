# 1
mi_listado = ["manzana", "pera", "plátano"]

# 2
mi_valor = None

# 3
try:
    mi_valor = mi_listado[2000]
except IndexError:
    # 4
    mi_valor = "Esa posición del listado no existe"

# 5
print(mi_valor)
