def init():

    fla = list()
    vas = list()
    flu = list()
    bot = list()
    outros = list()
    salfla = list()
    salvas = list()
    salflu = list()
    salbot = list()
    saloutros = list()
    
    qOut = 0 


    while True:
        clube = input("Qual o seu clube de futebol de preferência?\n1 – Flamengo\n2 – Vasco\n3 – Fluminense\n4 – Botafogo\n5 – Outros\n")
        if clube == "0":
            break
        salario = input("Qual o seu salário? ")
        if clube == "0":
            break
        cidade = input("Qual a sua cidade natal?\n1 – Niterói\n2 – Outra\n")
        if clube == "0":
            break

        if clube == "1":
            fla.append(clube)
            fla.append(salario)
            salfla.append(salario)
            fla.append(cidade)

        if clube == "2":
            vas.append(clube)
            vas.append(salario)
            salvas.append(salario)
            vas.append(cidade)

        if clube == "3":
            flu.append(clube)
            flu.append(salario)
            salflu.append(salario)
            flu.append(cidade)

        if clube == "4":
            bot.append(clube)
            bot.append(salario)
            salbot.append(salario)
            bot.append(cidade)

        if clube == "5":
            outros.append(clube)
            outros.append(salario)
            saloutros.append(salario)
            outros.append(cidade)
            if cidade == "1":
                qOut = qOut + 1

    calNum(fla,1)
    calNum(vas,2)
    calNum(flu,3)
    calNum(bot,4)
    calNum(outros,5)

    calSal(salfla, 1)
    calSal(salvas,2)
    calSal(salflu,3)
    calSal(salbot,4)
    calSal(saloutros,5)

    todos = 0.0

    todos = todos + float(calAll(fla))
    todos = todos + float(calAll(vas))
    todos = todos + float(calAll(flu))
    todos = todos + float(calAll(bot))
    todos = todos + float(calAll(outros))

    print(f"Total de pessoas entrevistadas: {todos}")

def calNum(lista, x):
    a = 0
    for i in lista:
        a = a+1

    if x == 1:
        print(f"Torcedores do flamengo: {a/3}")
    if x == 2:
        print(f"Torcedores do vasco: {a/3}")
    if x == 3:
        print(f"Torcedores do fluminense: {a/3}")
    if x == 4:
        print(f"Torcedores do botafogo: {a/3}")
    if x == 5:
        print(f"Torcedores de outros times: {a/3}")

def calSal(lista, x):
    a = 0
    salario = 0.0

    for i in lista:
        salario = salario + float(i)
        a = a+1

    if a == 0:
        a=1
    if x == 1:
        print(f"Média salarial do flamengo: {salario/a}")
    elif x == 2:
        print(f"Média salarial do vasco: {salario/a}")
    elif x == 3:
        print(f"Média salarial do fluminense: {salario/a}")
    elif x == 4:
        print(f"Média salarial do botafogo: {salario/a}")
    else:
        print(f"Média salarial de outros times: {salario/a}")



def calAll(lista):
    a = 0
    for i in lista:
        a = a+1

    a = a/3
    return a

init()