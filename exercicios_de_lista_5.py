import random
listadeNumeros = []
Par = []
Impar = []

for i in range(20):
    listadeNumeros.append(random.randint(1, 50))

for i in listadeNumeros:
    if i % 2 == 0:
        Par.append(i)

    else:
        Impar.append(i)

print("Todos os Numeros",listadeNumeros)
print("Numeros Pares",Par)
print("Numeros Impar",Impar)