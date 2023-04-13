alturas = []
idades = []

for i in range(5):
    idade = int(input(f"Informe a idade do(a) {i+1}ª pessoa: "))
    altura = float(input(f"Informe a altura do(a) {i+1}ª pessoa: "))
    alturas.append(altura)
    idades.append(idade)

print("Idades em ordem inversa:")
for idade in reversed(idades):
    print(idade)

print("Alturas em ordem inversa:")
for altura in reversed(alturas):
    print("{:.2f}m".format(altura))
