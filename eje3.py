def sumatoria_pares(limite):
    suma = 0
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

num_limite = int(input("Ingrese el número límite para la suma de pares: "))
resultado = sumatoria_pares(num_limite)
print("La suma total de los números pares es:", resultado)