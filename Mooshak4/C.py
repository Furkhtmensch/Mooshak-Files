miradouro: str = input();
cidades: dict = {"ARCO DA VILA": "Faro", "GRACA": "Lisboa", "IGREJA DOS GRILOS": "Porto", "JARDINS DO PALACIO DE CRISTAL": "Porto", "MONTE AGUDO": "Lisboa", "MONTE DE FARO": "Faro", "PENHA DE FRANCA": "Lisboa", "SANTA CATARINA": "Lisboa", "SANTA LUZIA": "Lisboa", "SAO JORGE": "Lisboa", "SAO PEDRO DE ALCANTARA": "Lisboa", "SE CATEDRAL": "Porto", "SENHORA DO MONTE": "Lisboa", "SERRA DO PILAR": "Porto", "TORRE DOS CLERIGOS": "Porto", "VITORIA": "Porto"};
miradouros: dict = {"ARCO DA VILA": 0, "GRACA": 0, "IGREJA DOS GRILOS": 0, "JARDINS DO PALACIO DE CRISTAL": 0, "MONTE AGUDO": 0, "MONTE DE FARO": 0, "PENHA DE FRANCA": 0, "SANTA CATARINA": 0, "SANTA LUZIA": 0, "SAO JORGE": 0, "SAO PEDRO DE ALCANTARA": 0, "SE CATEDRAL": 0, "SENHORA DO MONTE": 0, "SERRA DO PILAR": 0, "TORRE DOS CLERIGOS": 0, "VITORIA": 0};
maximo: int = 0;
total: int = 0;

while (miradouro != "FIM"):
    total += 1;
    miradouros[miradouro] += 1;
    if (miradouros[miradouro] > maximo):
        maximo = miradouros[miradouro];
    miradouro = input();

print(total, maximo);

for key in cidades:
    if (miradouros[key] == maximo):
        print(key, cidades[key]);

