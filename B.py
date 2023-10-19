C, N = map(int , input().split())
counter = 0
lis = []
for i in range(N):
    P = int(input())
    D = input()
    if P <= C:
        lis.append(D)
        C -= P
        counter += P
for i in lis:
    print(i)
print(counter, C)