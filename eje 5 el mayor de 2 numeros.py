print("bienvenido")
num1 = int(input("ingresa un numero: "))
num2 = int(input("ingresa otro numero: "))
if num1 > num2:
    print(f"el numero mayor entre los 2 numeros es {num1}")
elif num2 > num1:
    print(f"el numero mayor entre los dos numeros es {num2}")
else:
    print("los numeros son iguales")