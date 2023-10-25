while True:
    senha = input("Coloque a senha que você deseja: ")   

    if len(senha) <= 8 and any(senha.isupper() for senha in senha) and any(senha.islower() for senha in senha) and any(senha.isdigit() for senha in senha):
        print("Senha válida")
        break
    else:
        print("Senha inválida, por favor, tente novamente.")

