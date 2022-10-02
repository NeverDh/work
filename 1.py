

r = int(input("Quantos números você quer? "))
i = 0
a = 0
vetor = list()
vetorP = list()

while i < r:

    vetor.append(float(input(f"{i+1}° número: ")))
    result = vetor[i]*vetor[i]
    vetorP.append(result)
    i = i+1

for c in vetorP:
    a = a + c
    
print(f"A soma dos quadrados é {a}")
