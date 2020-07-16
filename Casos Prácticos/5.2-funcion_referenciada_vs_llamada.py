# 1
def mi_funcion():
    print("Algo que hace mi_funcion")
    return "Valor de retorno de mi_funcion"

# 2
mi_funcion()

# 3
valor_retorno = mi_funcion()
print(valor_retorno)

# 4
funcion_referenciada = mi_funcion
print(funcion_referenciada)

# 5
valor_retornado_por_la_funcion_referenciada = funcion_referenciada()
print(valor_retornado_por_la_funcion_referenciada)
