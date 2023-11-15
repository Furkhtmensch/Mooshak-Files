n, r = map(int, input().split());
ligacoes: dict = {};

for i in range(r):
    origem, destino, lugares, preco = map(int, input().split());
    ligacoes[(origem, destino)] = [lugares, preco];

t = int(input());

for i in range(t):
    flag: bool = True;
    pagamento: int = 0;
    reserva: list = list(map(int, input().split()));
    for j in range(2, reserva[1] + 1):
        if ((reserva[j], reserva[j + 1]) not in ligacoes):
            print(f"({reserva[j]},{reserva[j + 1]}) inexistente");
            flag = False;
            break;
        elif (ligacoes[(reserva[j], reserva[j + 1])][0] - reserva[0] >= 0):
            ligacoes[(reserva[j],reserva[j + 1])][0] -= reserva[0];
            pagamento += ligacoes[(reserva[j], reserva[j + 1])][1]*reserva[0];
        else:
            print(f"Sem lugares suficientes em ({reserva[j]},{reserva[j + 1]})");
            flag = False;
            break;
    if (flag):
        print("Total a pagar:", pagamento);
    else:
        for k in range(2, j):
            ligacoes[(reserva[k],reserva[k + 1])][0] += reserva[0];




