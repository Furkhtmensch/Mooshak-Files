C, L = map(int, input().split())
lajes = []
counter = 0
direito = True
pontos = 0

for i in range(L):
    lajes.append(int(input()))
    counter += 1
    if counter == C:
        if direito:
            pontos += max(lajes)
            counter -= lajes.index(max(lajes)) + 1
            del lajes[0:lajes.index(max(lajes)) + 1]
        else:
            pontos -= min(lajes)
            counter -= lajes.index(min(lajes)) + 1
            del lajes[0:lajes.index(min(lajes)) + 1]
        direito = not direito
if counter > 0:    
    if direito:
        pontos += max(lajes)

print(pontos)
    
