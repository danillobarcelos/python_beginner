import random
import numpy as np

range_x = random.randint(0,100)
range_y = random.randint(0,100)
lista_x = np.random.randint(0, 100, (range_x))
lista_y = np.random.randint(0, 100, (range_y))

#print(lista_x)
#print(lista_y)

lista_z = []

for i in lista_x:
    if i in lista_y:
        lista_z.append(i)

print(f"Os elementos da primeira lista são: {lista_x}")
print(f"Os elementos da segunda lista são: {lista_y}")
print(f"Os elementos em comum nas duas listas são: {lista_z}")

print(len(lista_x))
print(len(lista_y))
print(len(lista_z))