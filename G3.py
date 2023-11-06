L, C = map(int, input().split());
matriz = [list(map(int, input().split())) for _ in range(L)];
alvo = matriz[0][0];
i: int = 0;
j: int = 0;
caminho: str = '_';
soma: int = alvo;

while (True):
    if (i + 1 < L and caminho[-1] != 'C'):
        if (matriz[i + 1][j] == alvo):
            caminho += 'B';
            i += 1;
            soma += alvo;
            continue;
    if (i - 1 > -1 and caminho[-1] != 'B'):
        if (matriz[i - 1][j] == alvo):
            caminho += 'C';
            i -= 1;
            soma += alvo;
            continue;
    if (j + 1 < C and caminho[-1] != 'E'):
        if (matriz[i][j + 1] == alvo):
            caminho += 'D';
            j += 1;
            soma += alvo;
            continue;
    if (j - 1 > -1 and caminho[-1] != 'D'):
        if (matriz[i][j - 1] == alvo):
            caminho += 'E';
            j -= 1;
            soma += alvo;
            continue;
    break;

print(caminho[1::]);
print(soma);
