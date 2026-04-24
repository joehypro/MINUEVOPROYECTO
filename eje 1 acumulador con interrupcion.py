print("sumador automatico (usa 0 para terminar).")
suma = 0
while True:
    numero = int(input("Ingresa un numero entero: "))
    if numero == 0:
        break
    suma = suma + numero
print(f"la suma total es: {suma}")
