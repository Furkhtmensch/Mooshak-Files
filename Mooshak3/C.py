k: str = input();
resultado: str = k;

while (True):
    k += input();
    if (k[1] == '#'):
        break;
    elif (k[0] == k[1]): resultado += k[1];
    elif ('a' not in k): resultado += 'a';
    elif ('c' not in k): resultado += 'c';
    else: resultado += 't';
    k = k[1];

for i in resultado:
    print(i);




