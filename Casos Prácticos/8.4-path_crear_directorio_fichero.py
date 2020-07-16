from pathlib import Path


ruta_hasta_dir = "ruta/NuevoDir/"

obj_ruta_dir = Path(ruta_hasta_dir)

# 1
if obj_ruta_dir.exists():
    print("El directorio '{}' ya existe".format(obj_ruta_dir.name))
else:
    print("El directorio '{}' NO existe, "
          "por lo que se creará uno nuevo".format(obj_ruta_dir.name))

    # 2
    obj_ruta_dir.mkdir()

    #  ruta/NuevoDir/nuevo_fichero.txt
    obj_ruta_dir_fichero = obj_ruta_dir / Path("nuevo_fichero.txt")
    obj_ruta_dir_fichero.touch()
