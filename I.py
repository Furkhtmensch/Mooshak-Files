moedas = list(map(int, input().split()))
tipos = [200, 100, 50, 20, 10, 5]

a = -1
b = -1
erro = 0
transacoes = 0
retencoes = 0

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    transacoes += 1
    preco = a*100 + b
    c = -1
    pagamento = 0

    while c != 0:
        if c == 50 or c == 20 or c == 10 or c == 5:
            if c == 50:
                moedas[2] += 1
            elif c == 20:
                moedas[3] += 1
            elif c == 10:
                moedas[4] += 1
            else:
                moedas[5] += 1
            pagamento += c
        elif c == 2 or c == 1:
            if c == 2:
                moedas[0] += 1
            else:
                moedas[1] += 1
            pagamento += c*100
        c = int(input())

    troco = pagamento - preco

    for i in range(len(tipos)):
        while troco - tipos[i] >= 0 and moedas[i] > 0:
            troco -= tipos[i]
            moedas[i] -= 1

        if troco == 0:
            break

    if troco != 0:
        erro += troco
        troco = 0
        retencoes += 1

print(erro // 100, erro % 100)
print(str(retencoes) + "/" + str(transacoes))
