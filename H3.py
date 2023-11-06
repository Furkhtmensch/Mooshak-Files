L, C = map(int, input().split());
matriz: list = [input() for _ in range(L)];
K = int(input());
alvos: list = [input() for _ in range(K)];
horizontal: bool = False;
vertical: bool = False;
diagonal: bool = False;

def encontrar_inicial():
    candidatos: list = [];
    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            if matriz[k][l] == alvo[0]:
                candidatos.append([k, l]);
    return candidatos;

def encontrar_horizontal(direcao):
    construcao: str = alvo[0:2];
    for k in range(j + 2*direcao, len(matriz[i])*(direcao == 1) - 1*(direcao == -1), direcao):
        construcao += matriz[i][k];
        if (construcao not in alvo):
            return False;
        if (construcao == alvo):
            print(i + 1, j + 1, i + 1, k + 1);
            return True;

def encontrar_vertical(direcao):
    construcao: str = alvo[0:2];
    for k in range(i + 2*direcao, len(matriz)*(direcao == 1) - 1*(direcao == -1), direcao):
        construcao += matriz[k][j];
        if (construcao not in alvo):
            return False;
        if (construcao == alvo):
            print(i + 1, j + 1, k + 1, j + 1);
            return True;

def encontrar_diagonal(direcao_i, direcao_j):
    construcao: str = alvo[0:2];
    for k, l in zip(range(i + 2*direcao_i, len(matriz)*(direcao_i == 1) - 1*(direcao_i == -1), direcao_i), range(j + 2*direcao_j, len(matriz[i])*(direcao_j == 1) - 1*(direcao_j == -1), direcao_j)):
        construcao += matriz[k][l];
        if (construcao not in alvo):
            return False;
        if (construcao == alvo):
            print(i + 1, j + 1, k + 1, l + 1);
            return True;

for alvo in alvos:
    candidatos: list = encontrar_inicial();
    contador: int = 0;
    for candidato in candidatos:
        i, j = candidato[0], candidato[1];
        if (i + 1 < L):
            if (matriz[i + 1][j] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_vertical(1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 + 1, j + 1);
        if (i - 1 > -1):
            if (matriz[i - 1][j] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_vertical(-1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 - 1, j + 1);
        if (j + 1 < C):
            if (matriz[i][j + 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_horizontal(1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1, j + 1 + 1);
        if (j - 1 > -1):
            if (matriz[i][j - 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_horizontal(-1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1, j + 1 - 1);
        if (i + 1 < L and j + 1 < C):
            if (matriz[i + 1][j + 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_diagonal(1, 1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 + 1, j + 1 + 1);
        if (i - 1 > -1 and j + 1 < C):
            if (matriz[i - 1][j + 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_diagonal(-1, 1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 - 1, j + 1 + 1);
        if (i + 1 < L and j - 1 > -1):
            if (matriz[i + 1][j - 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_diagonal(1, -1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 + 1, j + 1 + 1);
        if (i - 1 > -1 and j - 1 > -1):
            if (matriz[i - 1][j - 1] == alvo[1]):
                if (len(alvo) > 2):
                    if (encontrar_diagonal(-1, -1)):
                        break;
                else:
                    print(i + 1, j + 1, i + 1 - 1, j + 1 - 1);


