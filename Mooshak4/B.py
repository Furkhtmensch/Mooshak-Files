T, N = map(int, input().split());
trajetos: list = [];
nos: dict = {};

for i in range(1, N + 1):
    nos[i] = [];

for i in range(T):
    soma: int = 0;
    trajetos.append(list(map(int, input().split())));
    for j in range(1, len(trajetos[i])):
        if (j + 2 < len(trajetos[i]) and j % 2 != 0):
            if (trajetos[i][j + 2] not in nos[trajetos[i][j]]):
                nos[trajetos[i][j]].append(trajetos[i][j + 2]);
            if (trajetos[i][j] not in nos[trajetos[i][j + 2]]):
                nos[trajetos[i][j + 2]].append(trajetos[i][j]);
        if (j % 2 == 0):
            soma += trajetos[i][j];
    print(f"Trajeto {i + 1}:", soma);

contador: int = 1;
for key in nos:
    print(f"No {contador}:", len(nos[key]));
    contador += 1;
