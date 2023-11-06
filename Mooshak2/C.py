n = int(input())
lis1 = list(map(int, input().split()))
lis2 = list(map(int, input().split()))

cons = 0
pontos = 0
counter = 0

for i in range(n):
    if lis1[i] == lis2[i]:
        cons += 1
        counter += 1
    elif cons == 1:
        pontos += cons
        cons = 0
    elif cons > 1:
        pontos += cons*3
        cons = 0
if cons == 1:
    pontos += cons
    cons = 0
elif cons > 1:
    pontos += cons*3
    cons = 0

print(counter)
print(pontos)