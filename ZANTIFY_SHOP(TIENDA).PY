cesta = []
precios = []
total_objetos = 0

print("-" * 30)
print("   ZANTIFY SHOP   ")
print("-" * 30)

corriendo = True

while corriendo:
    print("\nMENU DE OPCIONES:")
    print("1. AGREGAR producto")
    print("2. MOSTRAR cesta")
    print("3. ELIMINAR producto")
    print("4. CALCULAR total")
    print("5. TERMINAR")

    opcion = input("Escoge una de ellas (1-5): ")

    if opcion == "1":
        item = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cesta.append(item)
        precios.append(precio)
        print("Producto agregado")
        total_objetos = total_objetos + 1
    
    elif opcion == "2":
        if total_objetos == 0:
            print("Cesta vacia")
        else:
            for i in range(total_objetos):
                print("-" + cesta[i])
    
    elif opcion == "3":
        if total_objetos == 0:
            print("Nada que eliminar")
        else:
            borrar = input("Que quieres eliminar?: ")
            if borrar in cesta:
                posicion = cesta.index(borrar)
                precios.pop(posicion)
                cesta.remove(borrar)
                total_objetos = total_objetos - 1
                print("Obejto eliminado")
            else:
                print("No encontrado")
    
    elif opcion == "4":
        suma = 0
        for p in precios:
            suma = suma + p
        print("Total: $" + str(suma))
    
    elif opcion == "5":
        corriendo = False
    
    else:
        prin("Error")
