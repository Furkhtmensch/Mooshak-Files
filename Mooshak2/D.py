n = int(input())
m = list(map(int, input().split()))
isalex = True
isbela = False
A = 0
B = 0
for i in range(n):
    if isalex:
        A += m[-(m[0] < m[-1])]
        del m[-(m[0] < m[-1])]
        isalex = not isalex
    else:
        B += m[-((isbela) != (m[0] > m[-1]))]
        del m[-((isbela) != (m[0] > m[-1]))]
        isbela = not isbela
        isalex = not isalex

if A > B:
    print(f"Alex ganha com {A} contra {B}")
elif A < B:
    print(f"Bela ganha com {B} contra {A}")
else:
    print(f"Alex e Bela empatam a {A}")

            