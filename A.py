n = int(input())
min = 8
max = 18
for i in range(n):
    min1, max1 = map(int, input().split())
    if max1 < max: max = max1
    if min1 > min: min = min1
if max - min < 0:
    print("impossivel")
elif (max + min) / 2  == (max + min) // 2:
    print((max + min) // 2)
else:
    print((max + min) // 2, "e meia")