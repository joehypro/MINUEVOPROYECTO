parrafo = "maIcra eS bueno y proGramar en pYthon tambien es Bueno".lower().split()
frecuencia = {}
for pal in parrafo:
    frecuencia[pal] = frecuencia.get(pal, 0) + 1
print(frecuencia)