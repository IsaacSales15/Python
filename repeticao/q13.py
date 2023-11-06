while True:
    n = int(input("Digite um número inteiro positivo menor que 16: "))
    
    if n >= 16:
        print("O número deve ser menor que 16.")
    else:
        f = 1
        p = 1

        while p <= n:
            f *= p
            p += 1

        print(f)
