temps = []

while True:
    temp = int(input("Coloque a temperatura que deseja (ou digite 0 para finalizar): "))
    
    if temp == 0:
        print("Finalizado!")
        break
    else:
        temps.append(temp)

if temps:
    menor_temp = min(temps)
    maior_temp = max(temps)
    media = sum(temps) / len(temps)
    print(f"A menor temperatura foi: {menor_temp}°C, a  maior temperatura foi: {maior_temp}°C e a média das temperaturas foi: {media:.2f}°C.")
else:
    print("Nenhuma temperatura foi inserida.")
