def calcular_suscripcion(precio_mensual, meses):
    total = precio_mensual * meses
    if meses >= 6:
        total = total * 0.85
    return total

precio = float(input("Ingrese el precio mensual del paquete: "))
tiempo = int(input("Ingrese la cantidad de meses a contratar: "))
resultado = calcular_suscripcion(precio, tiempo)
print("El total a pagar es:", resultado)