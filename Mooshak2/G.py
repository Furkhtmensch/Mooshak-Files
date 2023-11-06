N = int(input())

for i in range(N):
    n = int(input())
    k = None
    counter = 1
    previous = None
    check = True
    valores = list(map(int, input().split()))
    for i in range(n):
        if valores[i] != -1 and previous == None:
            if valores[i] < i and i != 0:
                check = False
                break
            previous = valores[i]
        elif valores[i] != -1:
            if k == None:
                k = (valores[i] - previous) / counter
                if int(k) != k or k <= 0 or (valores[i] < i*k and valores[0] == -1):
                    check = False
                    break
            else:
                if k != (valores[i] - previous) / counter:
                    check = False
                    break
            counter = 1
            previous = valores[i]
        elif valores[i] == -1 and previous != None:
            counter += 1
    if check == True:
        print("Possivel")
    else:
        print("Impossivel")
        
            
    