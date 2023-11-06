n = int(input("Digite um número: "))

while n < 0 or n > 10:
    n = int(input("Número inválido! Digite o número novamente: "))

else:
    print("Número válido!")