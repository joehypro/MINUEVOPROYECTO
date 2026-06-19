alumnos = {"Johander": 6.5,"Rodrigo": 5.8, "Victoria": 7.0, "Jose": 4.5}
suma = 0
aprobados = 0
for nota in alumnos.values():
    suma += nota
    if nota >= 6.0:
        aprobados += 1
print(f"Promedio: {suma / len(alumnos):.2f}. Aprobados : {aprobados}")