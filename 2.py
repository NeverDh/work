numero1 = float(input("Primeiro numero: "))
numero2 = float(input("Segundo numero: "))
x = 0

while numero1 >= numero2:
    numero1 -= numero2
    x = x+1

print(f"O resultado da divisão é {x} e o resto é {numero1}")

