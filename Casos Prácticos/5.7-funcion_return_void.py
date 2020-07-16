def busca(cosa_a_buscar):
    listado_cosas = ["boligrafo", "taza", "cuchara"]

    for cosa in listado_cosas:
        if cosa == cosa_a_buscar:
            print("Encontrado")
            return

    print("No Encontrado")
    return  # El return vacío al final del cuerpo de la función se puede omitir

busca("taza")
busca("armario")
