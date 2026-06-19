personas = [("Johander",13),("Juan",25),("abuela",67)]
for nombre,edad in personas:
    if edad < 18:
        cat = "Menor"
    elif edad < 65:
        cat = "Adulto"
    else:
        cat = "Mayor"
    print(f"{nombre} es {cat}")