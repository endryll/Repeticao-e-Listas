MaiorNumero = None

for num in range(1, 6):
    num = (int(input("Digite um numero: ")))
    if MaiorNumero is None or num > MaiorNumero:
        MaiorNumero = num

print(f"Esse é maior numero digitado é: {MaiorNumero}")