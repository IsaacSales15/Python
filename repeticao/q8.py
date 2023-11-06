from functools import reduce
from operator import mul

numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}° número da lista: "))
    numeros.append(n)

print(f"A soma dos números foi: {sum(numeros)}, e a múltiplicação deles foi: {reduce(mul, numeros, 1)} ")