# 1 2
def imprimir_linea_recibo(producto, precio, multiplicador=1, descuento=None):
    if descuento:
        texto_descuento = "Descuento: {desc}".format(desc=descuento)
    else:
        texto_descuento = "No hay descuento"

    print("{producto} x {multiplicador} cuesta {precio}€ {texto_descuento}".format(producto=producto,
                                                                                   multiplicador=multiplicador,
                                                                                   precio=precio,
                                                                                   texto_descuento=texto_descuento))

# 3
imprimir_linea_recibo("Chorizo", 2)
imprimir_linea_recibo("Jabón", 1, descuento="5%", multiplicador=10)
imprimir_linea_recibo("Servilletas", 6, multiplicador=3, descuento="7%")
imprimir_linea_recibo("Chocolate", 3, multiplicador=6)
imprimir_linea_recibo("Lechuga", 4, descuento="3%")
imprimir_linea_recibo("Tomate", 3, 1, "10%")
imprimir_linea_recibo("Jamón", 100, 2)
imprimir_linea_recibo("Galletas", 4)