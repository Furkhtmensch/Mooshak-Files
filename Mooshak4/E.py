elementos, origem, destino, hpartida, hchegada = map(int, input().split());
matriz: list = [];
n = int(input());

for i in range(n):
    matriz.append(list(map(int, input().split())));

k, h = map(int, input().split());
problemas_totais: list = [];

while (k != 0 or h != 0):
    problemas: int = 0;
    duracao: int = h*60;
    flag_origem: bool = False;
    flag_destino: bool = False;
    rotas = list(map(int, input().split()));
    for i in range(k - 1):
        if ((matriz[rotas[i*3] - 1][rotas[i*3 + 3] - 1] == 1)):
            problemas += 1;
        if (flag_origem or rotas[i*3] == origem):
            if (flag_origem):
                duracao += rotas[i*3 + 2];
            if (rotas[i*3 + 1] < elementos or duracao < hpartida*60 or duracao > hchegada*60):
                break;
            if (flag_origem == False):
                duracao += rotas[i*3 + 2];
                flag_origem = True;
            if (rotas[i*3 + 3] == destino):
                flag_destino = True;
                break;
        else:
            duracao += rotas[i*3 + 2];
    if (flag_destino):
        problemas_totais.append(problemas);
    k, h = map(int, input().split());

contador: int = 0;

if (len(problemas_totais) > 0):
    minimo: int = min(problemas_totais);
    for i in problemas_totais:
        if (i == minimo):
            contador += 1;
    print(contador, minimo);
else:
    print("Impossivel");



