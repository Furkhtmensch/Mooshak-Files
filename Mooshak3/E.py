sons: list = ["jaco", "muuu", "miao", "auau", "meemee"];
som: str = input();
total: int = 0;
minimo: int = 0;
maximo: int = 0;

while (som != '0'):
    contador: int = 0;
    total += 1;
    if (som[0] == '2'):
        maximo += 1;
        for i in sons:
            if (i in som[2::] or len(som[2::]) > 9):
                minimo += 1;
                break;
    som = input();

print(total, minimo, maximo);

