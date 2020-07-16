# 1
lanzar_excepcion = "value"  # "value", "index", "buffer"

# 3
try:
    # 2
    if lanzar_excepcion == "value":
        raise ValueError("He lanzado la excepción ValueError")
    elif lanzar_excepcion == "index":
        raise IndexError("He lanzado la excepción IndexError")
    else:
        raise BufferError("He lanzado una excepción BufferError")
except ValueError as mi_error:
    print(mi_error)
    print("Capturada ValueError")
except IndexError as mi_error:
    print(mi_error)
    print("Capturada IndexError")
except Exception as mi_error:
    print(mi_error)
    print("Capturada cuelquier otra")
