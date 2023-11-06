C, N = map(int , input().split())
counter = 0
for i in range(N):
    P = int(input())
    D = input()
    if P <= C:
        print(D)
        C -= P
        counter += P
print(counter, C)
