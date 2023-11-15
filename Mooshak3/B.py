N, M = map(int, input().split());
restored: list = [0 for _ in range(M)];
restored_string: str = '';

for _ in range(N):
    temporary: str = input();
    for i in range(M):
        if (temporary[i] == '1'): restored[i] += 1;

for i in range(M):
    if (restored[i] > (N / 2)): restored_string += '1';
    else: restored_string += '0';

print(restored_string);





