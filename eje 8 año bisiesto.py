print("bienvenido")
num1 = int(input("ingresa un año para saber si es bisiesto: "))
if num1 % 4 == 0 and not num1 % 100 == 0 or num1 % 400 == 0:
    print("es bisiesto")
else:
    print("no es bisiesto")
