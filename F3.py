n: int = int(input());
inacessiveis: int = n;
gaveta_anterior: str = input();
if (gaveta_anterior == 'o'):
    inacessiveis -= 1;

for i in range(n - 1):
    gaveta_atual: str = input();
    if (gaveta_atual == 'o'):
        inacessiveis -= 1;
    else:
        if (gaveta_anterior == 'o'):
            inacessiveis -= 1;
    gaveta_anterior = gaveta_atual;

print(inacessiveis);