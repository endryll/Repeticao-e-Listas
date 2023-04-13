vetor = []
somadosquadrados = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)
    somadosquadrados += numero ** 2

print(f"A soma dos quadrados é: {somadosquadrados}")