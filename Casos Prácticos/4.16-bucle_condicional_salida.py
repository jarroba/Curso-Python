# 1
continua = True

# 2
uno = False
dos = False
tres = False

# 3
while continua:
    # 4
    print("uno: {}, dos: {}, tres: {}".format(uno, dos, tres))

    # 5
    if not uno:
        uno = True
    elif not dos:
        dos = True
    elif not tres:
        tres = True
    else:
        continua = False
