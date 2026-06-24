def contar_vocales(frase):
    contador = 0
    vocales = "aeiouAEIOU"
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

texto_usuario = input("Ingrese una frase para contar sus vocales: ")
resultado = contar_vocales(texto_usuario)
print("El número total de vocales es:", resultado)