def es_primo(n):
    if n < 2:
        for i in range(2, int(2,n**0.5) + 1 ):
            if n % i == 0:
                return False
        return True
if es_primo(11):
    print("es primo")
else:
    print("no es primo")