numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um numero: ")))

MaiorNumero = numeros[0]
cont = 1

while cont < len(numeros):
    if numeros[cont] > MaiorNumero:
        MaiorNumero = numeros[cont]
    cont = cont + 1

print(f"Esse é maior numero digitado é: {MaiorNumero}")