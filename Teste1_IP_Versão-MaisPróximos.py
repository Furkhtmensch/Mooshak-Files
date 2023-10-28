


# 1.- a)

'''

7 24 14

'''



# 1.- b)

'''

k = 4
c = 3
k = 6
2*a = 20
k = 8
c = 0
k = 10

'''



# 2.- a)

def traduzir(p):
    if p >= 500:
        print("Chuva violenta")
    elif p >= 100:
        print("Chuva forte")
    elif p >= 25:
        print("Chuva moderada")
    elif p > 0:
        print("Chuva fraca")
    else:
        print("Sem chuva")



# 2.- b)

'''

n = int(input())
while n != -1:
    traduzir(n)
    n = int(input())

'''



# 3.-

def maxcons(a, b, n):
    contador = 0
    max = 0
    for i in range(n):
        valor = int(input())
        if valor >= a and valor <= b:
            contador += 1
            if max < contador:
                max = contador
        else:
            contador = 0
    return max



# 4.- a)

''' A variável primelist serve para criar a lista de primos de 2 a 1000, não faz parte do teste, serve apenas para testar a função. '''

primelist = []
test = True
for num in range(2, 1001):
    for i in range(2, num):
        if num % i == 0:
            test = False
            break
    if test:
        primelist.append(num)
    test =  True

def fatoriza(n, primos = primelist):
    lis = []
    for i in primos:
        while n % i == 0:
            lis.append(i)
            n = n // i
        if n == 1:
            break
    if n != 1:
        lis.append(n)
    return lis



# 4.- b)

def mdcfact(fa, fb):
    lis = []
    for i in range(len(fa)):
        for j in range(len(fb)):
            if fa[i] < fb[0]:
                break
            if fa[i] == fb[j]:
                lis.append(fa[i])
                del fb[0:j + 1]
                break
    if lis == []:
        return [1]
    return lis



# 5.-

def maisproximos():
    x, y, n = map(int, input().split())
    a, b = map(int, input().split())
    dmp = (x - a)**2 + (y - b)**2
    lis = [[a, b]]
    for i in range(n - 1):
        a, b = map(int, input().split())
        if (x - a)**2 + (y - b)**2 < dmp:
            dmp = (x - a)**2 + (y - b)**2
            lis = [[a, b]]
        elif (x - a)**2 + (y - b)**2 == dmp:
            lis.append([[a, b]])
    return lis


