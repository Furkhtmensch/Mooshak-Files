dinheiro, linhas, colunas = map(int, input().split());
matriz: list = [];
direcoes: dict = {'E': [0, 1], 'W': [0, -1], 'N': [-1, 0], 'S': [1, 0]};

for _ in range(linhas):
    matriz.append(input());
    
n = int(input());
movimentos: list = [];

for _ in range(n):
    movimentos.append(input());

i: int = linhas - 2;
j: int = 1;
flag: bool = False;
desnorteado: str = 'ND';
emigrar: bool = False;

def acoes(acao: str) -> None:
    global dinheiro, direcoes, flag, desnorteado, emigrar, i, j;
    if (acao == 'T'):
        dinheiro -= dinheiro // 10;
    elif (acao == 'I'):
        dinheiro += dinheiro // 20;
    elif (acao == 'X'):
        direcoes['N'][0] = -direcoes['N'][0];
        direcoes['S'][0] = -direcoes['S'][0];
        if (desnorteado == 'ND'):
            desnorteado = 'D';
        else:
            desnorteado = 'ND';
    elif (acao == 'F'):
        flag = True;
        print("Aniquilado");
    elif (acao == 'A'):
        emigrar = True;
        
for k in range(n):
    for _ in range(int(movimentos[k][1])):
        i += direcoes[movimentos[k][0]][0];
        j += direcoes[movimentos[k][0]][1];
        if (i == linhas - 1):
            i -= 1;
            if (desnorteado == 'D'):
                desnorteado = 'ND';
                direcoes['N'][0] = -direcoes['N'][0];
                direcoes['S'][0] = -direcoes['S'][0];
            break;
        if (j == 0):
            j += 1;
            if (desnorteado == 'D'):
                desnorteado = 'ND';
                direcoes['N'][0] = -direcoes['N'][0];
                direcoes['S'][0] = -direcoes['S'][0];
            break;
        if (i > 0 and j < colunas - 1 and j > 0 and i < linhas - 1):
            emigrar = False;
        if (i >= 0 and j <= colunas - 1 and j >= 0 and i <= linhas - 1):
            acoes(matriz[i][j]);
        if (i <= 0 or j >= colunas - 1):
            dinheiro += 10;
        if (flag):
            break;
    if (flag):
        break;

if (not flag):
    if (emigrar):
        print(f"Fora({j},{linhas - 1 - i}):{dinheiro}:{desnorteado}");
    else:
        print(f"Dentro({j},{linhas - 1 - i}):{dinheiro}:{desnorteado}");


