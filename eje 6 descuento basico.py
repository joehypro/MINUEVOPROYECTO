print("bienvenido")
num1 = float(input("ingresa el monto: "))
if num1 >= 100:
     descuento = num1 * 0.15
     resultado = num1 - descuento
     print(f"se aplico el descuento ahorraste: ${descuento}")
     print(f"el total a pagar es: ${resultado}")
else:
     print("el monto es menor a $100 asi que no hay descuento")
