numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}° número da lista: "))
    numeros.append(n)

p = sum(y % 2 == 0 for y in numeros)
im = sum(w % 2 != 0 for w in numeros) 

print(f"Números pares: {p}")
print(f"Números ímpares: {im}")