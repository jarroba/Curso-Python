recetas = {
    "tortilla": ["patatas", "huevos", "aceite", "sal"],
    "ensalada": ["tomate", "lechuga", "aceite", "vinagre", "sal"],
    "macarrones": ["pasta", "tomate", "queso"],
    "pizza": ["pan", "tomate", "queso", "peperoni"]
}

# 1
recetas_str = ", ".join(recetas.keys())
print("Todos nuestros platos son: {}".format(recetas_str))

# 2
for ingredientes in recetas.values():
    print(ingredientes)

# 3
for nombre, ingredientes in recetas.items():
    str_ingredientes = "\n * ".join(ingredientes)
    print(" == {} ==\n * {}".format(nombre, str_ingredientes))
