while True:
    try:
        pessoas_que_fazem_o_L = float(input("Informe a população inicial do país A: "))
        crescimentoA = float(input("Informe a taxa de crescimento do país A: "))
        pessoas_que_nao_fazem_o_L = float(input("Informe a população inicial do país B: "))
        crescimentoB = float(input("Informe a taxa de crescimento do país B: "))

        if all(x >= 0 for x in [pessoas_que_fazem_o_L, crescimentoA, pessoas_que_nao_fazem_o_L, crescimentoB]):
            anos_sem_picanha = 0

            while pessoas_que_fazem_o_L < pessoas_que_nao_fazem_o_L:
                pessoas_que_fazem_o_L += pessoas_que_fazem_o_L * crescimentoA
                pessoas_que_nao_fazem_o_L += pessoas_que_nao_fazem_o_L * crescimentoB
                anos_sem_picanha += 1

            print(f"Em cerca de {anos_sem_picanha} anos, a população do país B será de {pessoas_que_nao_fazem_o_L}, e a população do país A será {pessoas_que_fazem_o_L} (faz o L agora)")

            dnovo = input("Deseja repetir essa ação? (s/n): ")
            if dnovo != 's':
                break
        else:
            print("Por favor, insira valores positivos.")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
