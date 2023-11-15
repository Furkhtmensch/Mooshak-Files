L, C = map(int, input().split());
fita: str = '';
i: int = 9999;
flag: bool = True;
L += 1;

for _ in range(C):
    fita += input();

while (True):
    flag = True;
    if (C // i == C / i):
        for j in range(0, (C - C // i)*L, (C // i)*L):
            if (fita[j:j + (C // i)*L] != fita[j + (C // i)*L: j + L*2*(C // i)]):
                flag = False;
                break;
        if (flag):
            print(i);
            break;
    i -= 1;




