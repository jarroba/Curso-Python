# 1
texto_unicode = "Camión"
print(texto_unicode)

# 2
texto_a_bytes = texto_unicode.encode("utf-8")
print(texto_a_bytes)

# 3
texto_windows1252 = texto_a_bytes.decode("windows-1252")
print(texto_windows1252)
