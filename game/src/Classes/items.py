atk = 18
multiplier = 1.22
lista = []
for _ in range(10):
    lista.append(atk)
    atk = atk * multiplier
    atk = int(atk)
print(lista)