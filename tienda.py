def mostrar_menu():
    print("\n" + "X" * 30)
    print("    ZANTIFY GEAR SHOP   ")
    print("X" * 30)
    print("1. AGREGAR Equipo (Sensor, Lente, etc.)")
    print("2. VER Inventario de Cesta")
    print("3. ELIMINAR Ítem Defectuoso")
    print("4. TOTAL de la Factura")
    print("5. SALIR")
def agregar_item(cesta):
    nombre = input("Nombre del artículo: ")
    while True:
        precio_txt = input(f"Precio de {nombre}: ")
        if precio_txt.replace('.', '', 1).isdigit():
            precio = float(precio_txt)
            break
        print("Error Mete un número válido.")
    
    item = {"item": nombre, "costo": precio}
    cesta.append(item)
    print(f"-> {nombre} añadido.")
def ver_cesta(cesta):
    print("\n--- TU INVENTARIO ---")
    if not cesta:
        print("Vacio...")
    else:
        for i, art in enumerate(cesta, 1):
            print(f"{i}. {art['item']} - ${art['costo']:.2f}")
def calcular(cesta):
    total = sum(art['costo'] for art in cesta)
    print(f"\nTOTAL A PAGAR: ${total:.2f}")
mi_cesta = []
while True:
    mostrar_menu()
    op = input("Opción: ")
    if op == '1':
        agregar_item(mi_cesta)
    elif op == '2':
        ver_cesta(mi_cesta)
    elif op == '3':
        if mi_cesta:
            ver_cesta(mi_cesta)
            idx = int(input("Número a borrar: ")) - 1
            borrado = mi_cesta.pop(idx)
            print(f"Eliminado: {borrado['item']}")
        else: print("Nada que borrar.")
    elif op == '4':
        calcular(mi_cesta)
    elif op == '5':
        print("Suerte en la tormenta")
        break