texto: str = input();
contador: int = 0;
for i in texto:
    if (i == "p") or (i == "P"): contador += 1;
print(contador);