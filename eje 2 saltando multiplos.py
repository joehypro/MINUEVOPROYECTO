print("numeros del 1 al 20 sin contar multiplos de 3")
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)