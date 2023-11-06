matriz: list = [input() for _ in range(6)];
candidatos: list = [];
candidatos_linhas: list = [];

for i in range(7):
    for j in range(6):
        if (matriz[j][i] != '.'):
            candidatos.append(matriz[j][i]);
            candidatos_linhas.append(j);
            break;
    if (len(candidatos) <= i):
        candidatos.append('.');
        candidatos_linhas.append(0);

def verificar_colunas():
    for i in range(7):
        contador: int = 0;
        if candidatos[i] != '.':
            for j in range(candidatos_linhas[i], 6):
                if (matriz[j][i] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
            if (contador == 4):
                print(f"GANHOU {candidatos[i]}");
                return True;
    return False;

def verificar_linhas():
    for i in range(7):
        contador: int = 0;
        if candidatos[i] != '.':
            for j in range(i, 7):
                if (matriz[candidatos_linhas[i]][j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;
            contador = 0;
            for j in range(i, -1, -1):
                if (matriz[candidatos_linhas[i]][j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;

    return False;

def verificar_diagonais():
    for i in range(7):
        contador: int = 0;
        if candidatos[i] != '.':
            for j in range(4):
                if (candidatos_linhas[i] < j or i < j):
                    break;
                if (matriz[candidatos_linhas[i] - j][i - j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;
            contador = 0;
            for j in range(4):
                if (candidatos_linhas[i] + j > 5 or i < j):
                    break;
                if (matriz[candidatos_linhas[i] + j][i - j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;
            contador = 0;
            for j in range(4):
                if (candidatos_linhas[i] < j or i + j > 6):
                    break;
                if (matriz[candidatos_linhas[i] - j][i + j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;
            contador = 0;
            for j in range(4):
                if (candidatos_linhas[i] + j > 5 or i + j > 6):
                    break;
                if (matriz[candidatos_linhas[i] + j][i + j] == candidatos[i]):
                    contador += 1;
                else:
                    contador = 0;
                if (contador == 4):
                    print(f"GANHOU {candidatos[i]}");
                    return True;
    return False;


if (not (verificar_colunas() or verificar_linhas() or verificar_diagonais())):
    check: bool = True;
    for i in matriz:
        if ('.' in i):
            print("JOGANDO");
            check = False;
            break;
    if (check):
        print("EMPATE");
    


