print("bienvenido")
num1 = float(input("introduce el primer lado: "))
num2 = float(input("introduce el segundo lado: "))
num3 = float(input("introduce el tercer lado: "))
if num1 == num2 and num2 == num3:
    print("el triangulo es equilatero")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print ("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")