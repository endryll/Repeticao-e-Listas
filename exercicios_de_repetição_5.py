print("Insira a população da A:")
populacao_a = int(input())
print("Insira a população da B:")
populacao_b = int(input())
print("Insira o crescimento da A:")
taxa_a = float(input())

while taxa_a < 0:
    print("Número inválido")
    taxa_a = float(input())
print("Insira o crescimento da B:")
taxa_b = float(input())

while taxa_b < 0:
    print("Número inválido")
    taxa_b = float(input())

ano = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * (taxa_a / 100)
    populacao_b += populacao_b * (taxa_b / 100)
    ano += 1

print(f"Em {ano} anos, a população de A ({populacao_a:.0f}) ultrapassará ou igualará a população de B ({populacao_b:.0f}).")
