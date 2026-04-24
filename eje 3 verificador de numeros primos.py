numero = int(input("ingresa un numero para saber si es primo: "))
if numero > 1:
    for i in range(2,numero):
        if numero % i == 0:
            print(f"{numero} no es primo porque su divisor es {i}")
            break
    else:
        print(f"{numero} es un numero primo")
else:
    print("no es primo")