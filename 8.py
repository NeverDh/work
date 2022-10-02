
boo = False
while boo == False:
    operacao = input("Digite  a operação: \n1. Somar\n2. Subtrair\n3. Dividir\n4. Multiplicar\n5. Sair\n")
    if operacao == '5':
        break
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = 0
    if operacao == '1':
        resultado = float(numero1) + float(numero2)
    if operacao == '2':
        resultado = float(numero1) - float(numero2)
    if operacao == '3':
        resultado = float(numero1) / float(numero2)
    if operacao == '4':
        resultado = float(numero1) * float(numero2)
    if operacao == '5':
        boo == True

    print("Resultado da operação: ", resultado, "\n")