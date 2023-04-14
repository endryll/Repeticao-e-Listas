nome = input("Digite o nome de usuário: ")

while True:
    senha = str(input("Digite a senha: "))
    if nome == senha:
        print("Senha inválida! A senha deve ser diferente do nome do usuário.")
    else:
        print("Senha valida")
        break