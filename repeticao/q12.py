n = int(input("Número: "))

f = 1
p = 1

while p <= n:
    f *= p
    p += 1
    
print(f)