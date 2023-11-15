nos, ramos = map(int, input().split());
rede: dict = {};
percurso: list = [];

for _ in range(ramos):
    extremo_1, extremo_2, temperatura, custo = map(int, input().split());
    rede[(extremo_1, extremo_2)] = temperatura;
    rede[(extremo_2, extremo_1)] = temperatura;

while (True):
    maximo: int = -50;
    minimo: int = 50;
    temperatura_atual: int = 0;
    percurso = list(map(int, input().split()));
    if (percurso == [0]):
        break;
    del percurso[0];
    for i in range(len(percurso) - 1):
        temperatura_atual = rede[(percurso[i], percurso[i + 1])];
        if (temperatura_atual == None):
            continue;
        if (temperatura_atual > maximo):
            maximo = temperatura_atual;
        if (temperatura_atual < minimo):
            minimo = temperatura_atual;
    print(minimo, maximo);








