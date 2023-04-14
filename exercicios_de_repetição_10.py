numero1=int(input("digite o primeiro número: "))
numero2=int(input("digite o segundo número: "))

while numero2<numero1:
    numero1=int(input("digite o primeiro número: "))
    numero2=int(input("digite segundo número: "))
else:
    for i in range(numero1,numero2,1):
        print(i)