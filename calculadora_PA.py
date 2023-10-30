t1 = int(input("Coloque o primeiro termo da P.A: "))
t2 = int(input("Coloque o segundo termo da P.A: "))

r = t2 - t1

def calcular_Termos(t1, r):
    for i in range(10):
        f = t1 + i * r
        print(f)
    
if r < 0:
    print(f"A sua P.A é DECRESCENTE, a razão é {r} e os 10 primeiros termos são: ")
    calcular_Termos(t1, r)
    
elif r > 0:
    print(f"A sua P.A é CRESCENTE, a razão é {r} e os 10 primeiros termos são: ")
    calcular_Termos(t1, r)

else:
    print("Razão igual a 0!")
