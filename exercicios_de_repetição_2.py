while True:
    nome = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite a senha: "))
    if nome == senha:
        print("Senha inválida! A senha deve ser diferente do nome do usuário.")
    else:
        print("Login válido")
        break