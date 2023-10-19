lis = []
n = -1

while True:
    n = int(input())
    if n == 0:
        break
    if n in lis:
        for i in range(len(lis)):
            if lis[i] == n:
                lis = lis[0:i]
                break
    lis.append(n)
for i in lis:
    print(i)

