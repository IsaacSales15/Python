nome = input("Digite o seu nome: ")
senha = input("Digite a sua senha: ")

while nome == senha:
    senha = input("Senha inválida! Digite a sua senha novamente: ")
    
else:
    print("Senha e nome válidos")