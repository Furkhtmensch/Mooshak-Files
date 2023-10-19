n = int(input())
tipos = []
quantidade = []
sentados = 0
restantes = 0

for i in range(n):
    tipos.append(int(input()))
    quantidade.append(int(input()))

n = int(input())

for i in range(n):
    N = int(input())
    oti = True
    for j in range(N):
        T = int(input())
        if oti == True:
            if T in tipos:
                index = tipos.index(T)
                if quantidade[index] > 0:
                    quantidade[index] -= 1
                    sentados += 1
                    oti = False

for i in quantidade:
    restantes += i

print(n - sentados)
print(restantes)
        
