

n = int(input("Quantos termos você quer? "))

antes = 0
depois = 1
soma = 1

for n in range(n):
    print(antes)
    soma = antes + depois
    antes = depois
    depois = soma