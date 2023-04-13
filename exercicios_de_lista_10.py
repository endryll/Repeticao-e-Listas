vetor_1 = []
vetor_2 = []


for i in range(10):
    valor = int(input("Digite um valor para o primeiro vetor: "))
    vetor_1.append(valor)
    valor = int(input("Digite um valor para o segundo vetor: "))
    vetor_2.append(valor)

vetor_3 = []

for i in range(10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print("Terceiro vetor intercalado:", vetor_3)