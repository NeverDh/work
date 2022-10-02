x = int(input("Quantos Nuggets você quer comprar? "))

i = 0
result = False

seis = 6
nove = 9
vinte = 20

a =0

while i <= x:
    if x%6 == 0:
        i = i+seis
        if i == x:
            result=True
            break
    elif x%9 == 0:
        i = i+nove
        if i == x:
            result=True
            break
    elif x%20 == 0:
        i = i+vinte
        if i == x:
            result=True
            break
    else:
        result = False
        break

a = 0

while not i<=x:
    a= a+1
    if i+6 <= x:
        i = i+seis
        a=a+1
        if i == x:
            break

    elif i+9 <= x:
        i = i+nove
        a=a+1
        if i == x:
            break

    elif i+20 <= x:
        i = i+vinte
        a=a+1
        if i == x:
            break
    elif a == 100:
        break


print(result)
