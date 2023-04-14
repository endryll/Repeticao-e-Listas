while True:
    nome = str(input("Digite seu nome: "))
    if len(nome) <= 3:
        print("Seu nome deve ter mais que 3 caracteres: ")
    else:
        break

while True:
    idade = int(input("Digite sua idade: "))
    if (idade < 0) or (idade > 150):
        print("Voce deve ter entre 0 e 150 anos: ")
    else:
        break

while True:
    salario = float(input("Digite seu Salário: "))
    if (salario < 0):
        print("Seu sálario não pode ser negativo: ")
    else:
        break

while True:
    sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
    if (sexo!= 'f') and (sexo!= 'm'):
        print("você deve ser 'f' ou 'm': ")
    else:
        break

while True:
    civil = input("Estado civil (s, c, v ou d): ")
    if (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
        print("Deve ser s, c, v ou d: ")
    else:
        break