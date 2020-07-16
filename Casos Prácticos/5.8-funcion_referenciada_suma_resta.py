# 1
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

# 2
if input("Algo suma, nada resta:"):
    funcion_referenciamos = suma
else:
    funcion_referenciamos = resta

a = int(input("a = "))
b = int(input("b = "))

resultado = funcion_referenciamos(a, b)
print(resultado)
