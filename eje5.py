def filtrar_masas(pesos_gramos):
    pesos_kilogramos = []
    for peso in pesos_gramos:
        kg = peso / 1000
        if kg >= 0.585:
            pesos_kilogramos.append(kg)
    return pesos_kilogramos

entrada = input("Ingrese los pesos en gramos separados por un espacio: ")
lista_gramos = [float(x) for x in entrada.split()]
resultado = filtrar_masas(lista_gramos)
print("Pesos válidos en kilogramos:", resultado)