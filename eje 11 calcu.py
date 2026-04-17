print("bienvenido")
numero1 = float(input("introduce un numero: "))
numero2 = float(input("introduce otro numero: "))
signo = input("elije un signo para tu operacion (+, -, *, /): ")
if signo == "+":
    resultado = numero1 + numero2
    print(f"el resultado de tu suma es: {resultado}")
elif signo == "-":
    resultado = numero1 - numero2
    print(f"el resultado de tu resta es: {resultado}")
elif signo == "*":
    resultado = numero1 * numero2
    print(f"el resultado de tu multiplicacion es: {resultado}")
elif signo == "/":
    if numero2 == 0:
        print("ojala se pudiera dividir con 0")
    else:
        resultado = numero1 / numero2
        print("el resultado de tu division es: ")
else:
    print("error,pon un signo valido pls")