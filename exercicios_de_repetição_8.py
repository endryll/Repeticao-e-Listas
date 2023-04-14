media = 0
soma = 0

for i in range(5):
    num = float(input("Digite um número: "))
    soma += num

media = soma / 5

print(f"soma: {soma}")
print(f"média: {media}")