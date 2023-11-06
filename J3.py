expressao: str = input();
abertura: list = [];
fecho: list = [];
abertura_tipo: list = [];
fecho_tipo: list = [];

for i in range(len(expressao)):
    if (expressao[i] == '(' or expressao[i] == '[' or expressao[i] == '{'):
        abertura.append(i);
        abertura_tipo.append(expressao[i]);
    elif (expressao[i] == ')' or expressao[i] == ']' or expressao[i] == '}'):
        fecho.append(i);
        fecho_tipo.append(expressao[i]);

if (abertura_tipo.count('[') != fecho_tipo.count(']') or abertura_tipo.count('(') != fecho_tipo.count(')') or abertura_tipo.count('{') != fecho_tipo.count('}')):
    print("Pares mal formados");
elif (len(abertura) == 0 and len(fecho) == 0):
    print("Sem noivos para casar");
else:
    for i in (fecho):
        maximo: int = 1001;
        rastreador: int = 0;
        for j in (abertura):
            if (i - j > 0 and i - j < maximo):
                maximo = i - j;
                rastreador = j;
        print(abertura_tipo[abertura.index(rastreador)] + fecho_tipo[fecho.index(i)], rastreador, i);
        del abertura_tipo[abertura.index(rastreador)];
        abertura.remove(rastreador);





