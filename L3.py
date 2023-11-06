n = int(input());
tonto: bool = False;
ind: int = 0;
direcoes: list = ["S", "SE", "E", "NE", "N", "NW", "W", "SW"];
sentido: int = 1;

while (n != -1):
    ind = (ind + (sentido*(n // 45))) % 8;
    if (n > 720):
        tonto = True;
        sentido = -sentido;
    else:
        tonto = False;
    n = int(input());

print(f"({direcoes[ind]}, " + "CW, "*(sentido == -1) + "CCW, "*(sentido == 1) + "normal"*(not tonto) + "tonto"*(tonto) + ")");
