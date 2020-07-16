# 1
enero = 100
febrero = -80
marzo = -240

# 2
total = enero + febrero + marzo

# 3
if total >= 0:
    texto_pagado = "Todo pagado"
else:
    texto_pagado = "Falta por pagar"

# 4
texto = "Ganancias/Perdidas\n" \
        "Enero: {enero}€\n" \
        "Febrero: {febrero}€\n" \
        "Marzo: {marzo}€\n" \
        "================\n" \
        "Total: {total}€\n" \
        "[{pagado}]".format(enero=enero,
                            febrero=febrero,
                            marzo=marzo,
                            total=total,
                            pagado=texto_pagado)
print(texto)
