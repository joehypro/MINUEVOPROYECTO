frase = input("Ingresa una palabra: ").lower()
contador = 0
for letra in frase:
    if letra in "aeiou":
        contador += 1
print(f"total: {contador}")