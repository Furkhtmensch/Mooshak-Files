par: list = [input(), input()];
novo_par: list = [[], []];

for i in range(2):
    for j in range(len(par[i])):
        if (97 <= ord(par[i][j].lower()) <= 122):
            novo_par[i].append(ord(par[i][j].lower()));
    novo_par[i].sort();

if (novo_par[0] == novo_par[1]): print("yes");
else: print("no");