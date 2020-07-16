# 1
piedra = False
papel = True
tijera = True

# 2
if papel and not tijera:
    print("Gana papel")
elif piedra and not papel:
    print("Gana piedra")
elif tijera and not piedra:
    print("Gana tijera")
else:
    print("No puede haber 3 jugadores")
