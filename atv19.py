nome = input("Coloque seu nome: ")
sexo = input("Insira seu sexo: (F) para feminino e (M) para masculino: ")
estado = input("Insira seu estado civil: casado(a) ou solteiro(a): ")

if sexo == "F" and estado == "casada":
    anos = int(input("Coloque seu tempo de casada (anos): "))
    print("Parabéns pelos seus ", anos, " de casada!")
elif sexo == "M" and estado == "casado":
    anos = int(input("Coloque seu tempo de casado (anos): "))
    print("Parabéns  pelos seus ", anos, " de casado!")
elif sexo == "M" and estado == "solteiro":
    print("Tenha fé, meu amigo, um dia você vai conseguir alguém")
elif sexo == "F" and estado == "solteira":
    print("Tenha fé, minha amiga, um dia você vai conseguir alguém")
else:
    print("Tu tá engraçado hoje, né?")

