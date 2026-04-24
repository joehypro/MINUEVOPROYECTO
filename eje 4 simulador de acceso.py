contra = "python123"
intentos = 0
print("logeate")
while intentos < 3:
    acceso = input("introduce la contraseña: ")
    if acceso == contra:
        print("acceso consedido,bienvenido")
        break
    else:
        intentos += 1
        restantes = 3 - intentos
        print(f"contraseña incorrecta. Te quedan {restantes} intentos.")
if intentos == 3:
    print("\nAcceso denegado")
    print("gastaste tus 3 intentos contacta al dev.")