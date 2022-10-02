from numpy import cbrt


p= 0
s = 0
divisor = 1
contador = 1

while contador <= 51:
    if contador % 2 == 0:
        s = s-1/pow(divisor, 3)
    else:
        s = s+1/pow(divisor, 3)
    
    divisor += 2
    contador = contador+1


p = cbrt(s * 32)

print(p)