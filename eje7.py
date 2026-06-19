def tabla_multiplicar_filtrada(base, limite):
    for numero in range(1, limite + 1):
        resultado = base * numero
        if resultado % 2 == 0:
            print(resultado)

num_base = int(input("Ingrese el número base de la tabla: "))
num_limite = int(input("Ingrese el límite de la tabla: "))
print("Resultados pares de la tabla:")
tabla_multiplicar_filtrada(num_base, num_limite)