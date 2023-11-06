n = int(input("Digite o n-ésimo termo da sequência: "))

f = [1,1]

for i in range(2, n):
    prox = f[-1] + f[-2]
    f.append(prox)
    
for termo in f:
    print(termo, end=" ")