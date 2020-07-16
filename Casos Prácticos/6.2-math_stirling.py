import math

# 1
num = 100

primera_parte = math.sqrt(2 * math.pi * num)
segunda_parte = math.pow(num/math.e, num)  # == (num / math.e) ** num

resultado = primera_parte * segunda_parte

print("Por fórmula de Stirling: {numero}!= {resultado}".format(numero=num,
                                                               resultado=resultado))

# 2
res_factorial = math.factorial(num)
print("Por fórumula normal: {numero}! = {resultado}".format(numero=num,
                                                            resultado=res_factorial))
