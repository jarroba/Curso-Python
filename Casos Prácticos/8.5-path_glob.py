from pathlib import Path


obj_ruta_dir = Path("C:\\Users\\rinva\\Documents\\MisArchivos\\")

# 1
lista_obj_ruta = obj_ruta_dir.glob("*")
for obj_ruta in lista_obj_ruta:
    print(obj_ruta)

# 2
lista_obj_ruta = obj_ruta_dir.glob("**/*")
for obj_ruta in lista_obj_ruta:
    print(obj_ruta)

# 3
lista_obj_ruta = obj_ruta_dir.glob("**/*.docx")
for obj_ruta in lista_obj_ruta:
    print(obj_ruta)
