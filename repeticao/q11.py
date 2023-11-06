n = 500

f = [0, 1]

while f[-1] <= n:
    prox = f[-1] + f[-2]
    f.append(prox)

for termo in f:
    print(termo, end=" ")