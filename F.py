B = int(input())
N = int(input())
V = B
amigos = []
justo = [0 for i in range(N)]
counter = 0

for i in range(N):
    p = int(input())
    amigos.append(p)


while True:
    for i in range(N):
        if justo[i] < amigos[i]:
            counter += 1
    if counter == 0:
        break
    elif V - counter >= 0:
        for i in range(N):
            if justo[i] < amigos[i]:
                justo[i] += 1
        V -= counter
        counter = 0
    else:
        break

if B // N == 0:
    for i in range(N):
        print(0)
else:
    for i in range(N):
        print(justo[i])
    
    
