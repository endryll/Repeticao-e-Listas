vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    valor = int(input("Digite um valor para o primeiro vetor: "))
    vetor_1.append(valor)
    valor = int(input("Digite um valor para o segundo vetor: "))
    vetor_2.append(valor)
    valor = int(input("Digite um valor para o terceiro vetor: "))
    vetor_3.append(valor)

intercalado = []

for i in range(10):
    intercalado.append(vetor_1[i])
    intercalado.append(vetor_2[i])
    intercalado.append(vetor_3[i])

print("Primeiro Vetor:", vetor_1)
print("Segundo Vetor:", vetor_2)
print("Terceiro Vetor:", vetor_3)
print("Vetores Intercalada:", intercalado)