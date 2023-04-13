Numeros = []

for i in range(5):
    Numeros.append(int(input("Informe os Numeros: ")))

soma = sum(Numeros)

multiplicacao = 1
for num in Numeros:
    multiplicacao *= num


print(f"Os números utilizados foram: {Numeros}")
print(f"A soma dos números: {soma}")
print(f"A multiplicação dos números: {multiplicacao}")