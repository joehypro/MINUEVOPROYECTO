def validar_contrasena(texto):
    if len(texto) > 8 and "@" in texto:
        return True
    else:
        return False

clave = input("Ingrese la contraseña a validar: ")
resultado = validar_contrasena(clave)
print("¿La contraseña es válida?:", resultado)