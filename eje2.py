def clasificar_calificaciones(notas):
    pasaron = 0
    reprobaron = 0
    for nota in notas:
        if nota >= 10:
            pasaron += 1
        else:
            reprobaron += 1
    return (pasaron, reprobaron)

entrada = input("Ingrese las notas separadas por un espacio: ")
lista_notas = [int(x) for x in entrada.split()]
resultado = clasificar_calificaciones(lista_notas)
print("Cantidad de aprobados y reprobados:", resultado)