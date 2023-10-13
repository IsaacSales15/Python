while True:
    n1 = float(input("Coloque a primerira nota: "))

    if n1 > 10 or n1 < 0:
        n1 = input("Nota inválida! Tente novamente: ")
    else:
        break

while True:
        n2 = float(input("Coloque a segunda nota: "))

        if n2 > 10 or n2 < 0:
            n2 = input("Nota inválida! Tente novamente: ")
        else:
            break

media = (n1 + n2)/2

print(media)

