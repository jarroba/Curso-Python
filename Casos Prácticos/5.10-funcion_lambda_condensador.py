# 1
def fun_energia_almacenada_condensador(capacidad, dif_potencial):
    return (1/2) * capacidad * dif_potencial ** 2

# 2
energia_almacenada_condensador = fun_energia_almacenada_condensador(3.0, 12)
print(energia_almacenada_condensador)

# 3
funlambda_energia_almacenada_condensador = lambda capacidad, dif_pot: (1/2)*capacidad*dif_pot**2
energia_almacenada_condensador = funlambda_energia_almacenada_condensador(3.0, 12)
print(energia_almacenada_condensador)
