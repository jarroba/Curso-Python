# 1
dic_pasteles = {
    "tarta": 12,
    "donut": 7,
    "magdalena": 9,
    "brownie": 9,
    "galleta": 254
}

# 2
print(len(dic_pasteles))

# 3
cantidad_tartas = dic_pasteles["tarta"]
print("Tenemos {} tartas".format(cantidad_tartas))

# 4
dic_pasteles["tarta"] += 5
cantidad_tartas_despues = dic_pasteles["tarta"]
print("Después tenemos {} tartas".format(cantidad_tartas_despues))

# 5
dic_pasteles["torrija"] = 20
print(len(dic_pasteles))

# 6
del dic_pasteles["brownie"]
print(len(dic_pasteles))
