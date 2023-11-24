def anoAluno(codigo: int) -> int:
    return codigo // 1000000;

def cursoAluno(codigo: int) -> int:
    return (codigo // 1000) % 100;

def ler_dados(nomefich: str) -> tuple:
    def ler_disciplinas() -> list:
        ndisc = int(f.readline());
        disciplinas: list = [];
        for _ in range(ndisc):
            nome: str = f.readline();
            ano = int(f.readline());
            nome = nome[0:len(nome) - 1];
            disciplinas.append((nome, ano));
        return disciplinas;
        
    def ler_dados_alunos() -> dict:
        nalunos = int(f.readline());
        alunos: dict = {};
        for _ in range(nalunos):
            nome: str = f.readline();
            linha = list(map(int, f.readline().split()));
            nome = nome[0:len(nome) - 1];
            alunos[linha[0]] = (nome, linha[1], linha[2:]);
        return alunos;
    try:
        f = open(nomefich, 'r');
    except IOError:
        return "O ficheiro especificado não existe";
    disc = ler_disciplinas();
    alunos = ler_dados_alunos();
    f.close();
    return (disc, alunos);

informacao: tuple = ler_dados("bdAlunos_fp7.txt");

def discAno(ano: int, disciplinas: list = informacao[0]) -> list:
    codigos: list = [];
    for i in range(len(disciplinas)):
        if (disciplinas[i][1] == ano):
            codigos.append(i + 1);
    return codigos;

def codigoAluno(nome: str, alunos: list = informacao[1]) -> list:
    codigos: list = [];
    for i in alunos:
        if (alunos[i][0][0:len(nome)] == nome):
            codigos.append(i);
    return codigos;

def media_ndisc(curso: int, alunos: list = informacao[1]) -> int:
    soma: int = 0;
    n: int = 0;
    for i in alunos:
        if (cursoAluno(i) == curso):
            soma += alunos[i][1];
            n += 1;
    if (n != 0):
        return soma // n;
    return 0;

def discAluno(codigo: int, nomefich: str = '', alunos: list = informacao[1], disciplinas: list = informacao[0]) -> None:
    if (nomefich != ''):
        t = open(nomefich, 'w');
        t.write("Disciplinas de" + ' ' + str(codigo) + ' ' + f"({alunos[codigo][0]}) \n");
    try:
        print("Disciplinas de", codigo, f"({alunos[codigo][0]})");
    except:
        print("Código invalido!");
        return;
    for i in range(alunos[codigo][1]):
        print(disciplinas[alunos[codigo][2][i] - 1][0]);
        if (nomefich != ''):
            t.write(disciplinas[alunos[codigo][2][i] - 1][0] + '\n');
    if (nomefich != ''):
        t.close();
    return;

def alunos_em_disc(disc: int, alunos: list = informacao[1], ndisc: int = len(informacao[0])) -> list:
    if (type(disc) != int or disc < 1 or disc > ndisc):
        raise TypeError;
    codigos: list = [];
    for i in alunos:
        if (disc in alunos[i][2]):
            codigos.append(i);
    return codigos;

def codigo_disc(nome, disciplinas: list = informacao[0]) -> int:
    for i in range(len(disciplinas)):
        if (nome == disciplinas[i][0]):
            return i + 1;
    raise ValueError;

def inscritos_disc(nome: str, disciplinas: list = informacao[0], alunos: list = informacao[1]) -> list:
    return alunos_em_disc(codigo_disc(nome, disciplinas), alunos);

def totais_por_disciplina(disciplinas: list = informacao[0], alunos: list = informacao[1]) -> None:
    contador: list = [0 for _ in range(len(disciplinas))];
    print("Numero de alunos inscritos\n");
    for i in alunos:
        for j in alunos[i][2]:
            contador[j - 1] += 1;
    for k in range(len(contador)):
        print(f"{disciplinas[k][0]}:", contador[k]);
    return;

def disc_populares(curso: int, disciplinas: list = informacao[0], alunos: list = informacao[1]) -> None:
    print(f"Disciplinas com mais alunos do curso {curso}\n");
    contador: list = [0 for _ in range(len(disciplinas))];
    for i in alunos:
        for j in alunos[i][2]:
            if (cursoAluno(i) == curso):
                contador[j - 1] += 1;
    maximo: int = max(contador);
    total: int = 0;
    for k in range(len(contador)):
        if (contador[k] == maximo):
            print(disciplinas[k][0]);
            total += 1;
    print();
    print(f"Total = {total}", f"Maximo = {maximo}");
    return;

def cursos_populares(disciplina: str, k: int, disciplinas: list = informacao[0], alunos: list = informacao[1]) -> None:
    contador: dict = {};
    for i in alunos:
        for j in alunos[i][2]:
            if (cursoAluno(i) not in contador):
                contador[cursoAluno(i)] = 1;
            else:
                contador[cursoAluno(i)] += 1;
    maximo: int = max(contador);
    print("Cursos existentes\n");
    for i in contador:
        print(i);
    print("Cursos com mais inscritos na disciplina especificada");
    for i in contador:
        if (contador[i] + k >= maximo):
            print(i);

menu = ["0 - terminar", "1 - carregar os dados a partir de um ficheiro", "2 - código de estudante dado o nome", "3 - disciplinas de estudante dado o código", "4 - disciplinas dado ano", "5 - número médio de disciplinas a que os alunos de dado curso estão inscritos", "6 - alunos que estão inscritos em dada disciplina (dado o código)", "7 - alunos que estão inscritos em dada disciplina (dado o nome)", "8 - número de alunos inscritos a cada disciplina", "9 - disciplinas que têm mais alunos de um dado curso", "10 - cursos que têm o maior número de alunos inscritos em uma dada disciplina (dado o nome da mesma) estando perto do maior por um dado k (alcance) de diferença/distância"];

def escolhe_menu() -> int:
    for s in menu:
        print(s);
    opcao = int(input("Indicar opção: "));
    while (opcao < 0 or opcao >= len(menu)):
        opcao = int(input("Opção inválida. Indicar opção: "));
    return opcao;

def interface() -> None:
    opcao: int = escolhe_menu();
    while (opcao != 0):
        if (opcao == 1):
            ficheiro: str = input("Ficheiro de dados? ");
            disciplinas, alunos = ler_dados(ficheiro);
        elif (opcao == 2):
            nome: str = input("Nome do estudante? ");
            print(codigoAluno(nome, alunos)[0]);
        elif (opcao == 3):
            codigo: int = int(input("Código do estudante? "));
            ficheiro: str = input("Ficheiro de resultados? ");
            discAluno(codigo, ficheiro, alunos, disciplinas);
        elif (opcao == 4):
            ano: int = int(input("Ano das disciplinas? "));
            print(discAno(ano, disciplinas));
        elif (opcao == 5):
            curso: int = int(input("Curso? "));
            print(media_ndisc(curso, alunos));
        elif (opcao == 6):
            disc: int = int(input("Número da disciplina? "));
            codigos: list = alunos_em_disc(disc, alunos, len(disciplinas));
            if (codigos == []):
                print("Nenhum");
            else:
                for i in codigos:
                    print(i);
        elif (opcao == 7):
            nome: str = input("Nome da disciplina? ");
            codigos: list = inscritos_disc(nome, disciplinas, alunos);
            if (codigos == []):
                print("Nenhum");
            else:
                for i in codigos:
                    print(i);
        elif (opcao == 8):
            totais_por_disciplina(disciplinas, alunos);
        elif (opcao == 9):
            curso: int = int(input("Número do curso? "));
            disc_populares(curso, disciplinas, alunos);
        elif (opcao == 10):
            disciplina: str = input("Nome da disciplina? ");
            k: int = int(input("Qual é o k (alcance)? "));
            cursos_populares(disciplina, k, disciplinas, alunos);
        else:
            print("Opção inválida. Tente de novo. ");
        opcao: int = escolhe_menu();
    
interface();
