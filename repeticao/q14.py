idades = []

while True:
    idade = int(input("Uma idade (ou digite 0 para finalizar): "))
    
    if idade == 0:
        print("Finalizado!")
        break
    else:
        idades.append(idade)

if idades:
    media = sum(idades) / len(idades)
    
    if 0 <= media <= 25:
        print("O grupo é de jovens")
    
    elif 25 < media <= 60:
        print("O grupo é de adultos")
        
    elif media > 60:
        print("O grupo é de idosos")
else:
    print("Nenhuma idade foi inserida.")
