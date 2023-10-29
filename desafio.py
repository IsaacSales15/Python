salarios = []
abonos = []

while True:
    s = float(input("Digite o salário (ou digite 0 para encerrar): "))

    if s == 0:
        print("Lista encerrada")
        break

    a = max(0.2 * s, 100)
    salarios.append(s)
    abonos.append(a)

for i in range(len(salarios)):
    print(f"Funcionário {i + 1}, salário: R${salarios[i]}, abono: R${abonos[i]}")

print(f"Total de funcionários processados: {len(salarios)}") 
print(f"Total gasto com abono: R${sum(abonos)}")
print(f"Maior valor de abono: R${max(abonos)}")