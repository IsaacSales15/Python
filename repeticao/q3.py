while True:
    n = input("Coloque o seu nome: ")
    i = int(input("Digite a sua idade: "))
    s = float(input("Digite o seu salário: "))
    sexo = input("Digite o seu sexo: [f] ou [m]: ")
    ec = input("Digite seu estado civil: [s], [c], [v] ou [d]: ")
    
    if len(n) > 3 and 0 <= i <= 150 and s > 0 and sexo in ["f", "m"] and ec in ["s", "c", "v", "d"]:
        print("Informações válidas!")
        break
    
    else:
        print("Informações inválidas!")