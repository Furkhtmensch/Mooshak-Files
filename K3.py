M, N = map(int, input().split());
matriz: list = [list(map(int, input().split())) for _ in range(M)];
memoria: list = []
contador: int = 0;
soma: int = 0;
construcao: list = [[[1, 0], [0, -1], [1, 0], [0, 1]], [[0, 1], [1, 0], [0, 1], [1, 0]], [[1, 0], [0, 1], [1, 0], [0, -1]], [[1,0], [0, -1], [0, -1], [1, 0]], [[1, 0], [0, -1], [1, 0], [0, 1]]];
teste: list = [];
desvios: int = 0;

def contar(i, j, continuation = False):
    global contador;
    global soma;
    global memoria;
    global construcao;
    global teste;
    global desvios;
    while (True):
        mudar_i: int = 0;
        mudar_j: int = 0;
        memoria.append([i, j]);
        verificador = False;
        if (i + 1 < M and [i + 1, j] not in memoria):
            if (matriz[i + 1][j] == 1):
                mudar_i += 1;
                soma += 1;
                verificador = True;
        if (i - 1 > -1 and [i - 1, j] not in memoria):
            if (matriz[i - 1][j] == 1):
                if (verificador):
                    soma += 1;
                    teste.append([-1, 0]);
                    desvios += 1;
                    contar(i - 1, j, True);
                    verificador = True;
                else:
                    mudar_i -= 1;
                    soma += 1;
                    verificador = True;
        if (j + 1 < N and [i, j + 1] not in memoria):
            if (matriz[i][j + 1] == 1):
                if (verificador):
                    soma += 1;
                    teste.append([0, 1]);
                    desvios += 1;
                    contar(i, j + 1, True);
                    verificador = True;
                else:
                    mudar_j += 1;
                    soma += 1;
                    verificador = True;
        if (j - 1 > -1 and [i, j - 1] not in memoria):
            if (matriz[i][j - 1] == 1):
                if (verificador):
                    soma += 1;
                    teste.append([0, -1]);
                    desvios += 1;
                    contar(i, j - 1, True);
                    verificador = True;
                else:
                    mudar_j -= 1;
                    soma += 1;
                    verificador = True;
        i += mudar_i;
        j += mudar_j;
        if (verificador == False):
            break;
        teste.append([mudar_i, mudar_j]);
    if (soma == 5 and continuation == False and desvios < 3 and desvios > 0):
        if teste in construcao:
            contador += 1;

for k in range(M):
    for l in range(N):
        soma = 0;
        teste = [];
        desvios = 0;
        if (matriz[k][l] == 1):
            soma += 1;
            contar(k, l);

print(contador);



