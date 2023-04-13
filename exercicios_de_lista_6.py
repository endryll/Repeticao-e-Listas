notas = []
nomes = []

for i in range(2):
    nome = input("Informe o nome do aluno: ")
    nomes.append(nome)
    soma = 0
    for j in range(4):
        nota = float(input(f"Informe a {j+1}ª nota do aluno ({nome}): "))
        soma += nota
    media = soma / 4
    notas.append(media)

contador = 0

for i in range(len(notas)):
    if notas[i] >= 7.0:
        contador += 1
        print(f"{nomes[i]} teve média {notas[i]:.1f} e foi aprovado(a).")

print(f"Existem {contador} alunos com média maior ou igual a 7.0.")